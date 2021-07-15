# sqlx-fetch_all

<div style="display:none">rust-tag-cnVzdC10YWc=</div>


```rust,no_run,noplaypen

# pub trait Executor<'c>: Send + Debug + Sized {
#    type Database: Database;

    /// Execute the query and return all the generated results, collected into a [`Vec`].
    fn fetch_all<'e, 'q: 'e, E: 'q>(
        self,
        query: E,
    ) -> BoxFuture<'e, Result<Vec<<Self::Database as Database>::Row>, Error>>
    where
        'c: 'e,
        E: Execute<'q, Self::Database>,
    {
        self.fetch(query).try_collect().boxed()
    }

    /// Execute the query and return the generated results as a stream.
    fn fetch<'e, 'q: 'e, E: 'q>(
        self,
        query: E,
    ) -> BoxStream<'e, Result<<Self::Database as Database>::Row, Error>>
    where
        'c: 'e,
        E: Execute<'q, Self::Database>,
    {
        self.fetch_many(query)
            .try_filter_map(|step| async move {
                Ok(match step {
                    Either::Left(_) => None,
                    Either::Right(row) => Some(row),
                })
            })
            .boxed()
    }



# }
```

fetch_many with AnyConnection

```rust,no_run,noplaypen
# impl<'c> Executor<'c> for &'c mut AnyConnection {
#    type Database = Any;

    fn fetch_many<'e, 'q: 'e, E: 'q>(
        self,
        mut query: E,
    ) -> BoxStream<'e, Result<Either<AnyDone, AnyRow>, Error>>
    where
        'c: 'e,
        E: Execute<'q, Self::Database>,
    {
        let arguments = query.take_arguments();
        let query = query.sql();

        match &mut self.0 {
            #[cfg(feature = "postgres")]
            AnyConnectionKind::Postgres(conn) => conn
                .fetch_many((query, arguments.map(Into::into)))
                .map_ok(|v| v.map_right(Into::into).map_left(Into::into))
                .boxed(),

            #[cfg(feature = "mysql")]
            AnyConnectionKind::MySql(conn) => conn
                .fetch_many((query, arguments.map(Into::into)))
                .map_ok(|v| v.map_right(Into::into).map_left(Into::into))
                .boxed(),

            #[cfg(feature = "sqlite")]
            AnyConnectionKind::Sqlite(conn) => conn
                .fetch_many((query, arguments.map(Into::into)))
                .map_ok(|v| v.map_right(Into::into).map_left(Into::into))
                .boxed(),

            #[cfg(feature = "mssql")]
            AnyConnectionKind::Mssql(conn) => conn
                .fetch_many((query, arguments.map(Into::into)))
                .map_ok(|v| v.map_right(Into::into).map_left(Into::into))
                .boxed(),
        }
    }
# }

```
fetch_many with PgConnection

```rust,no_run,noplaypen


# impl<'c> Executor<'c> for &'c mut PgConnection {
#    type Database = Postgres;

    fn fetch_many<'e, 'q: 'e, E: 'q>(
        self,
        mut query: E,
    ) -> BoxStream<'e, Result<Either<PgDone, PgRow>, Error>>
    where
        'c: 'e,
        E: Execute<'q, Self::Database>,
    {
        let sql = query.sql();
        let metadata = query.statement().map(|s| Arc::clone(&s.metadata));
        let arguments = query.take_arguments();
        let persistent = query.persistent();

        Box::pin(try_stream! {
            let s = self.run(sql, arguments, 0, persistent, metadata).await?;
            pin_mut!(s);

            while let Some(v) = s.try_next().await? {
                r#yield!(v);
            }

            Ok(())
        })
    }
# }

```
try_stream!

```rust,no_run,noplaypen


macro_rules! try_stream {
    ($($block:tt)*) => {
        crate::ext::async_stream::TryAsyncStream::new(move |mut sender| async move {
            macro_rules! r#yield {
                ($v:expr) => {
                    let _ = futures_util::sink::SinkExt::send(&mut sender, Ok($v)).await;
                }
            }

            $($block)*
        })
    }
}

```