# JDK 
> java 15.0.1 2020-10-20 <br>
> Java(TM) SE Runtime Environment (build 15.0.1+9-18) <br>
> Java HotSpot(TM) 64-Bit Server VM (build 15.0.1+9-18, mixed mode, sharing) <br>

---

1. Collection 类的底层数据结构
    + ArrayList  

        ```java
                /**
                * The array buffer into which the elements of the ArrayList are stored.
                * The capacity of the ArrayList is the length of this array buffer. Any
                * empty ArrayList with elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA
                * will be expanded to DEFAULT_CAPACITY when the first element is added.
                */
                transient Object[] elementData; // non-private to simplify nested class access

        ```
    + Vectoor 
        ```java
                /**
                * The array buffer into which the components of the vector are
                * stored. The capacity of the vector is the length of this array buffer,
                * and is at least large enough to contain all the vector's elements.
                *
                * <p>Any array elements following the last element in the Vector are null.
                *
                * @serial
                */
                @SuppressWarnings("serial") // Conditionally serializable
                protected Object[] elementData;
        ```
    + LinkedList
        ```java
                transient int size = 0;

                /**
                * Pointer to first node.
                */
                transient Node<E> first;

                /**
                * Pointer to last node.
                */
                transient Node<E> last;
        ```
    + HashSet
        ```java
            private transient HashMap<E,Object> map;
        ```
    + LinkedHashSet
        ```java
            public class LinkedHashSet<E>
            extends HashSet<E>
            implements Set<E>, Cloneable, java.io.Serializable {
            /**
            * Constructs a new, empty linked hash set with the specified initial
            * capacity and load factor.
            *
            * @param      initialCapacity the initial capacity of the linked hash set
            * @param      loadFactor      the load factor of the linked hash set
            * @throws     IllegalArgumentException  if the initial capacity is less
            *               than zero, or if the load factor is nonpositive
            */
            public LinkedHashSet(int initialCapacity, float loadFactor) {
                super(initialCapacity, loadFactor, true);
            }
            }
        ```
    + TreeSet
        ```java
            /**
            * The backing map.
            */
            private transient NavigableMap<E,Object> m;
            /**
            * Constructs a new, empty tree set, sorted according to the
            * natural ordering of its elements.  All elements inserted into
            * the set must implement the {@link Comparable} interface.
            * Furthermore, all such elements must be <i>mutually
            * comparable</i>: {@code e1.compareTo(e2)} must not throw a
            * {@code ClassCastException} for any elements {@code e1} and
            * {@code e2} in the set.  If the user attempts to add an element
            * to the set that violates this constraint (for example, the user
            * attempts to add a string element to a set whose elements are
            * integers), the {@code add} call will throw a
            * {@code ClassCastException}.
            */
            public TreeSet() {
                this(new TreeMap<>());
            }
        ```
    + HashMap
        ```java
        
            /**
            * Constructs an empty {@code HashMap} with the specified initial
            * capacity and load factor.
            *
            * @param  initialCapacity the initial capacity
            * @param  loadFactor      the load factor
            * @throws IllegalArgumentException if the initial capacity is negative
            *         or the load factor is nonpositive
            */
            public HashMap(int initialCapacity, float loadFactor) {
                if (initialCapacity < 0)
                    throw new IllegalArgumentException("Illegal initial capacity: " +
                                                    initialCapacity);
                if (initialCapacity > MAXIMUM_CAPACITY)
                    initialCapacity = MAXIMUM_CAPACITY;
                if (loadFactor <= 0 || Float.isNaN(loadFactor))
                    throw new IllegalArgumentException("Illegal load factor: " +
                                                    loadFactor);
                this.loadFactor = loadFactor;
                this.threshold = tableSizeFor(initialCapacity);
            }
        ```
    + LinkedHashMap
        ```java
            /**
            * Constructs an empty insertion-ordered {@code LinkedHashMap} instance
            * with the specified initial capacity and load factor.
            *
            * @param  initialCapacity the initial capacity
            * @param  loadFactor      the load factor
            * @throws IllegalArgumentException if the initial capacity is negative
            *         or the load factor is nonpositive
            */
            public LinkedHashMap(int initialCapacity, float loadFactor) {
                super(initialCapacity, loadFactor);
                accessOrder = false;
            }

        ```

    + TreeMap
        ```java
        public class TreeMap<K,V>
            extends AbstractMap<K,V>
            implements NavigableMap<K,V>, Cloneable, java.io.Serializable
        {}
        ```