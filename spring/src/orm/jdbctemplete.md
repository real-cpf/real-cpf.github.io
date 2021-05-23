# jdbctemplete

>  It simplifies the use of JDBC and helps to avoid common errors. It executes core JDBC workflow, leaving application code to provide SQL and extract results. This class executes SQL queries or updates, initiating iteration over ResultSets and catching JDBC exceptions and translating them to the generic


```java
// update
String sql = "update ...";
Object[] args = { ... };
int[] argTypes = { Types.VARCHAR, Types.VARCHAR, Types.VARCHAR };
return this.jdbcTemplate.update(sql, args, argTypes);

// for list
String sql = "select ...";
return this.jdbcTemplate.queryForList(sql);


// impl import org.springframework.jdbc.core.RowMapper;
	@Override
	public Data mapRow(ResultSet rs, int rowNum) throws SQLException {
		Data d = new Data();
		student.setValue(rs.getString("v1"));
		return d;
	}

// query mapper
String sql = "select ...";
Object[] args = { sno };
int[] argTypes = { Types.VARCHAR };
List<T> studentList = this.jdbcTemplate.query(sql, args, argTypes, new DataMapper());

```

#### SimpleJdbcTemplate
---

####  NamedParameterJdbcTemplate
---