# 数据库应用系统
## 课程要求
* 实体数量 >= 5
* OS、DBMS、开发语言不限

## 书评资讯
### 模块划分
* 图书信息管理
* 系统用户管理
* 用户数据管理

#### 图书信息管理
* 添加图书
* 修改图书信息

#### 系统用户管理
* 用户注册
* 修改用户信息
* 最新书评展现

#### 用户数据管理
* 增删书评
* 点赞图书
* 点赞书评

#### 数据库设计

##### Entity Relationship Diagram（E-R图）

![ER](https://raw.githubusercontent.com/Duerxin/SYSU-Book-Database-Course-Project/master/ER.png)

##### 具体设计

- books

<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>book_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>title</td><td>varchar(100)</td><td>NO</td><td></td><td>NULL</td><td></td></tr>
<tr><td>subtitle</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>origin_title</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>alt_title</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>author</td><td>char(20)</td><td>YES</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>image</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>translator</td><td>char(20)</td><td>YES</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>catalog</td><td>varchar(4000)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>summary</td><td>varchar(5000)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>publisher</td><td>char(20)</td><td>YES</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>pages</td><td>int(11)</td><td>NO</td><td></td><td>NULL</td><td></td></tr>
<tr><td>binding</td><td>varchar(10)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>rating</td><td>char(20)</td><td>YES</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>isbn10</td><td>char(10)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>isbn13</td><td>char(13)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>series</td><td>char(20)</td><td>YES</td><td>MUL</td><td>0</td><td></td></tr>
<tr><td>price</td><td>varchar(20)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>pubdate</td><td>varchar(50)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>url</td><td>varchar(50)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>alt</td><td>varchar(50)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>id</td><td>varchar(10)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>


* user

<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>user_id</td><td>int(11)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>user_name</td><td>char(20)</td><td>NO</td><td>UNI</td><td>NULL</td><td></td></tr>
<tr><td>password</td><td>char(20)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>mail</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>sex</td><td>char(1)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>birthday</td><td>date</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

*  author
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>author_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>author_name</td><td>varchar(30)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>author_introduction</td><td>varchar(1000)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

*  book_likes
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>book_likes_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>liker_id</td><td>int(11)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>book_id</td><td>char(20)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>time</td><td>timestamp</td><td>NO</td><td></td><td>CURRENT_TIMESTAMP</td><td></td></tr>
</table>
</body>
</html>

*  book_likes_count
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>book_id</td><td>char(20)</td><td>NO</td><td></td><td>NULL</td><td></td></tr>
<tr><td>likes_num</td><td>bigint(21)</td><td>NO</td><td></td><td>0</td><td></td></tr>
</table>
</body>
</html>

*  publisher
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>publisher_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>publisher_name</td><td>varchar(30)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>publisher_introduction</td><td>varchar(1000)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

*  rating
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>rating_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>max</td><td>tinyint(3) unsigned</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>numbers</td><td>int(11)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>average</td><td>decimal(3,2)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>min</td><td>tinyint(3) unsigned</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

*  review_likes
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>likes_id</td><td>int(11)</td><td>NO</td><td>PRI</td><td>NULL</td><td>auto_increment</td></tr>
<tr><td>liker_id</td><td>int(11)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>reviews</td><td>int(11)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>time</td><td>timestamp</td><td>NO</td><td></td><td>CURRENT_TIMESTAMP</td><td></td></tr>
</table>
</body>
</html>

*  review_likes_count
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>reviews</td><td>int(11)</td><td>NO</td><td></td><td>0</td><td></td></tr>
<tr><td>likes_num</td><td>bigint(21)</td><td>NO</td><td></td><td>0</td><td></td></tr>
</table>
</body>
</html>

*  reviews
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>review_id</td><td>int(11)</td><td>NO</td><td>PRI</td><td>NULL</td><td>auto_increment</td></tr>
<tr><td>reviewer_id</td><td>int(11)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>book_id</td><td>char(20)</td><td>NO</td><td>MUL</td><td>NULL</td><td></td></tr>
<tr><td>time</td><td>timestamp</td><td>NO</td><td></td><td>CURRENT_TIMESTAMP</td><td>on update CURRENT_TIMESTAMP</td></tr>
<tr><td>content</td><td>varchar(5000)</td><td>NO</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

*  serie
<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>
<tr><td>serie_id</td><td>char(20)</td><td>NO</td><td>PRI</td><td>NULL</td><td></td></tr>
<tr><td>serie_name</td><td>varchar(100)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>serie_douban_id</td><td>varchar(20)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>description</td><td>varchar(1000)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
<tr><td>volumes</td><td>int(11)</td><td>YES</td><td></td><td>NULL</td><td></td></tr>
</table>
</body>
</html>

