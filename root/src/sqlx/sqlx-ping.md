# ping
<div style="display:none">rust-tag-cnVzdC10YWc=</div>
with pg

```rust,no_run,noplaypen
    // this impl under pg
    fn ping(&mut self) -> BoxFuture<'_, Result<(), Error>> {
        // By sending a comment we avoid an error if the connection was in the middle of a rowset
        self.execute("/* SQLx ping */").map_ok(|_| ()).boxed()
    }
    // under Any db
    fn ping(&mut self) -> BoxFuture<'_, Result<(), Error>> {
        delegate_to_mut!(self.ping())
    }
```


delegate_to_mut!
```rust,no_run,noplaypen

macro_rules! delegate_to_mut {
    ($self:ident.$method:ident($($arg:ident),*)) => {
        match &mut $self.0 {
            #[cfg(feature = "postgres")]
            AnyConnectionKind::Postgres(conn) => conn.$method($($arg),*),

            #[cfg(feature = "mysql")]
            AnyConnectionKind::MySql(conn) => conn.$method($($arg),*),

            #[cfg(feature = "sqlite")]
            AnyConnectionKind::Sqlite(conn) => conn.$method($($arg),*),

            #[cfg(feature = "mssql")]
            AnyConnectionKind::Mssql(conn) => conn.$method($($arg),*),
        }
    };
}


```