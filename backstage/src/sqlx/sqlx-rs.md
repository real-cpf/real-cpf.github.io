# sqlx rust
<div style="display:none">rust-tag-cnVzdC10YWc=</div>


---
+ [sqlx::query](./sqlx-query-query.md)

```rust,editable
{{#include ./rust-sqlx-any-test.rs:7:18}}
```

+ [ping](./sqlx-ping.md)

```rust,editable
{{#include ./rust-sqlx-any-test.rs:23:27}}
```


+ pool  [fetch_all](./sqlx-fetch_all.md)

```rust,editable
{{#include ./rust-sqlx-any-test.rs:32:38}}
```

+ fail and recover

```rust,editable
{{#include ./rust-sqlx-any-test.rs:55:74}}
```

+ Make a SQL query that is mapped to a concrete type  use [FromRow](./sqlx-fromrow.md)
> `in my opinion , rust not usually used reflections but use a lot of macro and trait`

```rust,editable
{{#include ./from_row.rs:97:99}}
```

> then ,we can use `#[derive(sqlx::FromRow)]`