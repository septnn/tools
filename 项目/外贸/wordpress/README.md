# wordpress

- version 5.5
- plugins
    - WooCommerce 
    - WooCommerce Services
- themes
    - Hestia
    
## 源码修改

### wp-includes/class-wp.php

```php
# 解决由于url内中文导致404问题
list( $req_uri ) = explode( '?', $_SERVER['REQUEST_URI'] );
# =>
list( $req_uri ) = explode( '?', urldecode($_SERVER['REQUEST_URI']) );
```