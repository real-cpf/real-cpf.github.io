# query::Query


<div style="display:none">rust-tag-cnVzdC10YWc=</div>

[Query](https://github.com/ChenPufeng/sqlx/blob/77cdafe08a11afee2bf72e85afecd7317f6671df/sqlx-core/src/query.rs#L17)
```rust,no_run,noplaypen
/// Raw SQL query with bind parameters. Returned by [`query`][crate::query::query].
#[must_use = "query must be executed to affect database"]
pub struct Query<'q, DB: Database, A> {
    pub(crate) statement: Either<&'q str, &'q <DB as HasStatement<'q>>::Statement>,
    pub(crate) arguments: Option<A>,
    pub(crate) database: PhantomData<DB>,
    pub(crate) persistent: bool,
}

/// Make a SQL query.
pub fn query<DB>(sql: &str) -> Query<'_, DB, <DB as HasArguments<'_>>::Arguments>
where
    DB: Database,
{
    Query {
        //Zero-sized type used to mark things that "act like" they own a T.
        //Adding a PhantomData<T> field to your type tells the compiler that 
        //your type acts as though it stores a value of type T, even though it doesn't really. 
        //This information is used when computing certain safety properties.
        database: PhantomData,
        arguments: Some(Default::default()),
        //The enum Either with variants Left and Right is a general purpose sum type with two cases.
        //The Either type is symmetric and treats its variants the same way, without preference.
        //(For representing success or error, use the regular Result enum instead.)
        statement: Either::Left(sql),
        persistent: true,
    }
}
```

[try_map](https://github.com/ChenPufeng/sqlx/blob/77cdafe08a11afee2bf72e85afecd7317f6671df/sqlx-core/src/query.rs#L102)

```rust,no_run,noplaypen


# impl<'q, DB, A: Send> Query<'q, DB, A>
# where
#    DB: Database,
#    A: 'q + IntoArguments<'q, DB>,
# {

    /// Map each row in the result to another type.
    ///
    /// See [`try_map`](Query::try_map) for a fallible version of this method.
    ///
    /// The [`query_as`](super::query_as::query_as) method will construct a mapped query using
    /// a [`FromRow`](super::from_row::FromRow) implementation.
    #[inline]
    pub fn map<F, O>(self, f: F) -> Map<'q, DB, impl TryMapRow<DB, Output = O>, A>
    where
        F: MapRow<DB, Output = O>,
        O: Unpin,
    {
        self.try_map(MapRowAdapter(f))
    }
# }
```

[fetch_one](https://github.com/ChenPufeng/sqlx/blob/77cdafe08a11afee2bf72e85afecd7317f6671df/sqlx-core/src/query.rs#L319)

```rust,no_run,noplaypen

# impl<'q, DB, A: Send> Query<'q, DB, A>
# where
#     DB: Database,
#     A: 'q + IntoArguments<'q, DB>,
# {


   /// Execute the query and returns exactly one row.
    pub async fn fetch_one<'e, 'c: 'e, E>(self, executor: E) -> Result<O, Error>
    where
        'q: 'e,
        E: 'e + Executor<'c, Database = DB>,
        DB: 'e,
        F: 'e,
        O: 'e,
    {
        self.fetch_optional(executor)
            .and_then(|row| match row {
                Some(row) => future::ok(row),
                None => future::err(Error::RowNotFound),
            })
            .await
    }

    /// Execute the query and returns at most one row.
    pub async fn fetch_optional<'e, 'c: 'e, E>(mut self, executor: E) -> Result<Option<O>, Error>
    where
        'q: 'e,
        E: 'e + Executor<'c, Database = DB>,
        DB: 'e,
        F: 'e,
        O: 'e,
    {
        //  executor.fetch_optional need impl with target db like
        let row = executor.fetch_optional(self.inner).await?; pg、mysql、sqlite

        if let Some(row) = row {
            self.mapper.try_map_row(row).map(Some)
        } else {
            Ok(None)
        }
    }
# }
```
fetch_optional

```rust,no_run,noplaypen
    fn fetch_optional<'e, 'q: 'e, E: 'q>(
        self,
        mut query: E,
    ) -> BoxFuture<'e, Result<Option<AnyRow>, Error>>
    where
        'c: 'e,
        E: Execute<'q, Self::Database>,
    {
        let arguments = query.take_arguments();
        let query = query.sql();

        Box::pin(async move {
            Ok(match &mut self.0 {
                #[cfg(feature = "postgres")]
                AnyConnectionKind::Postgres(conn) => conn
                    .fetch_optional((query, arguments.map(Into::into)))
                    .await?
                    .map(Into::into),

                #[cfg(feature = "mysql")]
                AnyConnectionKind::MySql(conn) => conn
                    .fetch_optional((query, arguments.map(Into::into)))
                    .await?
                    .map(Into::into),

                #[cfg(feature = "sqlite")]
                AnyConnectionKind::Sqlite(conn) => conn
                    .fetch_optional((query, arguments.map(Into::into)))
                    .await?
                    .map(Into::into),

                #[cfg(feature = "mssql")]
                AnyConnectionKind::Mssql(conn) => conn
                    .fetch_optional((query, arguments.map(Into::into)))
                    .await?
                    .map(Into::into),
            })
        })
    }
```



[map_row](https://github.com/ChenPufeng/sqlx/blob/77cdafe08a11afee2bf72e85afecd7317f6671df/sqlx-core/src/query.rs#L447)

```rust,no_run,noplaypen
# #[allow(unused_macros)]
macro_rules! impl_map_row {
    ($DB:ident, $R:ident) => {
        impl<O: Unpin, F> crate::query::MapRow<$DB> for F
        where
            F: Send + FnMut($R) -> O,
        {
            type Output = O;

            fn map_row(&mut self, row: $R) -> O {
                (self)(row)
            }
        }

        impl<O: Unpin, F> crate::query::TryMapRow<$DB> for F
        where
            F: Send + FnMut($R) -> Result<O, crate::error::Error>,
        {
            type Output = O;

            fn try_map_row(&mut self, row: $R) -> Result<O, crate::error::Error> {
                (self)(row)
            }
        }
    };
}

```