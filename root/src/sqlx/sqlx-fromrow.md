# sqlx-fromrow
<div style="display:none">rust-tag-cnVzdC10YWc=</div>
[FromRow](https://github.com/launchbadge/sqlx/blob/c7cf104a8f6c0e61c2a72bf9631a0f079e0e94f4/sqlx-core/src/from_row.rs#L4)
---

  A record that can be built from a row returned by the database.
 
  In order to use [`query_as`] the output type must implement `FromRow`.
 
  ## Derivable
 
  This trait can be derived by SQLx for any struct. The generated implementation
  will consist of a sequence of calls to [`Row::try_get`] using the name from each
  struct field.
 
  ```rust,ignore
  #[derive(sqlx::FromRow)]
  struct User {
      id: i32,
      name: String,
  }
  ```
 
  ### Field attributes
 
  Several attributes can be specified to customize how each column in a row is read:
 
  #### `rename`
 
  When the name of a field in Rust does not match the name of its corresponding column,
  you can use the `rename` attribute to specify the name that the field has in the row.
  For example:
 
  ```rust,ignore
  #[derive(sqlx::FromRow)]
  struct User {
      id: i32,
      name: String,
      #[sqlx(rename = "description")]
      about_me: String
  }
  ```
 
  Given a query such as:
 
  ```sql
  SELECT id, name, description FROM users;
  ```
 
  will read the content of the column `description` into the field `about_me`.
 
  #### `rename_all`
  By default, field names are expected verbatim (with the exception of the raw identifier prefix `r#`, if present).
  Placed at the struct level, this attribute changes how the field name is mapped to its SQL column name:
 
  ```rust,ignore
  #[derive(sqlx::FromRow)]
  #[sqlx(rename_all = "camelCase")]
  struct UserPost {
      id: i32,
      // remapped to "userId"
      user_id: i32,
      contents: String
  }
  ```
 
  The supported values are `snake_case` (available if you have non-snake-case field names for some
  reason), `lowercase`, `UPPERCASE`, `camelCase`, `PascalCase`, `SCREAMING_SNAKE_CASE` and `kebab-case`.
  The styling of each option is intended to be an example of its behavior.
 
  #### `default`
 
  When your struct contains a field that is not present in your query,
  if the field type has an implementation for [`Default`],
  you can use the `default` attribute to assign the default value to said field.
  For example:
 
  ```rust,ignore
  #[derive(sqlx::FromRow)]
  struct User {
      id: i32,
      name: String,
      #[sqlx(default)]
      location: Option<String>
  }
  ```
 
  Given a query such as:
 
  ```sql
  SELECT id, name FROM users;
  ```
 
  will set the value of the field `location` to the default value of `Option<String>`,
  which is `None`.
 
  [`query_as`]: fn.query_as.html
  [`Row::try_get`]: trait.Row.html#method.try_get
