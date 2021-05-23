# mybatisplus


## ActiveRecord
> import com.baomidou.mybatisplus.extension.activerecord.Model;

```java
@TableName("demotable")
@Accessors(chain = true)
@EqualsAndHashCode(callSuper = true)
public class DemoTable extends Model<DemoTable> {

    private Long id;


    @Override
    protected Serializable pkVal() {

        return this.id;
    }
}
```