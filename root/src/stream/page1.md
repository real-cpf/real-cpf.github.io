# Stream 

+ ##  BOMInputStream
    > http://akini.mbnet.fi/java/unicodereader/UnicodeInputStream.java.txt
    > http://www.unicode.org/unicode/faq/utf_bom.html
    ```
   BOMs in byte length ordering:
   00 00 FE FF    = UTF-32, big-endian
   FF FE 00 00    = UTF-32, little-endian
   EF BB BF       = UTF-8,
   FE FF          = UTF-16, big-endian
   FF FE          = UTF-16, little-endian
    ```
    ```java,editable
     /**
    * Read-ahead four bytes and check for BOM marks. Extra bytes are
    * unread back to the stream, only BOM bytes are skipped.
    */
   protected void init() throws IOException {
      if (isInited) return;

      byte bom[] = new byte[BOM_SIZE];
      int n, unread;
      n = internalIn.read(bom, 0, bom.length);    //读掉头部字节 

     //下面进行匹配
      if ( (bom[0] == (byte)0x00) && (bom[1] == (byte)0x00) &&
                  (bom[2] == (byte)0xFE) && (bom[3] == (byte)0xFF) ) {
         encoding = "UTF-32BE";
         unread = n - 4;
      } else if ( (bom[0] == (byte)0xFF) && (bom[1] == (byte)0xFE) &&
                  (bom[2] == (byte)0x00) && (bom[3] == (byte)0x00) ) {
         encoding = "UTF-32LE";
         unread = n - 4;
      } else if (  (bom[0] == (byte)0xEF) && (bom[1] == (byte)0xBB) &&
            (bom[2] == (byte)0xBF) ) {
         encoding = "UTF-8";
         unread = n - 3;
      } else if ( (bom[0] == (byte)0xFE) && (bom[1] == (byte)0xFF) ) {
         encoding = "UTF-16BE";
         unread = n - 2;
      } else if ( (bom[0] == (byte)0xFF) && (bom[1] == (byte)0xFE) ) {
         encoding = "UTF-16LE";
         unread = n - 2;
      } else {
         // Unicode BOM mark not found, unread all bytes
         encoding = defaultEnc;
         unread = n;
      }      
      //System.out.println("read=" + n + ", unread=" + unread);
       // 回退
      if (unread > 0) internalIn.unread(bom, (n - unread), unread);

      isInited = true;
   }
    ```

+ ##  BOMInputStream
+ ##  BOMInputStream
