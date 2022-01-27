### 要求 2
#### 創 website 資料庫
```sql
create database website character set utf8mb4 collate utf8mb4_0900_ai_ci;

show databases;
```
![show-databases](https://images.plurk.com/3SJDpsIG0Whhse85KsqqNZ.jpg)
#### 創 member 表
```sql
use website;

create table member (
  id bigint auto_increment comment '獨立編號',
  name varchar(255) not null comment '姓名',
  username varchar(255) not null comment '帳戶名稱',
  password varchar(255) not null comment '帳戶密碼',
  follower_count int not null default 0 comment '追蹤者數量',
  time datetime not null default current_timestamp comment '註冊時間',
  primary key(id)
) character set utf8mb4 collate utf8mb4_0900_ai_ci;

describe member;
```
- column 預設會繼承 table 的 character set
- character 選 utf8mb4 → 因為要打中文，也可支持 emoji。
- collate 選 utfmb4_0900_ai_ci → 因為看到[這篇](https://dev.mysql.com/doc/refman/8.0/en/charset-server.html)官方文件。
  
![describe-member](https://images.plurk.com/78xPTQqbUuYRXj4NJgxA6E.jpg)
---
### 要求 3
#### 新增一筆 username、password 是 test 的資料，再隨意新增四筆資料。
```sql
insert into member(name, username, password, follower_count)
values('Test User', 'test', 'test', 1001);

insert into member(name, username, password, follower_count)
values('User01', 'test01', 'test01', 716),
('User02', 'test02', 'test02', 25),
('User03', 'test03', 'test03', 154),
('User04', 'test04', 'test04', 99);
```
#### 取得 member 所有資料
```sql
select * from member;
```
#### 發現因為剛剛是一次建了四筆資料所以註冊時間是一樣的，就先改了時間，想看排序的效果 XD||
```sql
update member set time = time - interval 1 day where id = 2;
update member set time = time - interval 1 hour where id = 3;
update member set time = time - interval 20 minute where id = 4;
update member set time = time - interval 30 second where id = 5;

select * from member;
```
![select-all-member](https://images.plurk.com/1YCJaL3jdqaXBubZoY2dHy.jpg)
#### 按照 time 欄位，近到遠排序
```sql
select * from member order by time desc;
```
![select-all-member-desc](https://images.plurk.com/49dduNu3DpFimv14GEDJ0Q.jpg)
#### 取得按 time 欄位，近到遠排序後第 2 ~ 4 共 3 筆資料
```sql
select * from member order by time desc limit 1, 3;
```
![select-2to4-member-desc](https://images.plurk.com/aJCbyTmzO0hGpQ1z63Oyw.jpg)
- 因為是 0-based index，假設要第 n 行，limit 的第一個參數要寫 n-1，第二個參數是共要幾筆資料。
#### 取得 username 是 test 的資料（先讓表格出現兩個 username 都同樣是 test 的人，想看效果 XD||）
```sql
update member set username = 'test' where id = 2;

select * from member where username = 'test';
```
![select-username-test](https://images.plurk.com/5TAKCugE4tVPW0b3a8IEwu.jpg)
#### 取得 username 是 test、password 也是 test 的資料
```sql
select * from member where username = 'test' and password = 'test';
```
![select-username-password-test](https://images.plurk.com/2HIG9NTopTcCKeioYqjXMw.jpg)
#### 把 username 是 test 的資料改 name 叫 test2
```sql
update member set username = 'test2' where username = 'test';

select * from member;
```
![update-username-testtotest2](https://images.plurk.com/2DRYTCd0yOBEFon1TIKsFC.jpg)
---
### 要求 4
#### 取得 member 共有幾筆資料
```sql
select count(*) from member;
```
![how-many-rows-member](https://images.plurk.com/2YGrVxwcnKQvgiwnsoMwqH.jpg)
#### 取得 member 所有會員追蹤者總和
```sql
select sum(follower_count) from member;
```
![sum-follower-count](https://images.plurk.com/4g4KejD3WnuixXlAUduVDV.jpg)
#### 取得 member 所有會員追蹤者平均數
```sql
select avg(follower_count) from member;
```
![avg-follower-count](https://images.plurk.com/3bqZe0v1bHqfEWN1J1oAEZ.jpg)
---
### 要求 5
#### 建 message 表（接著建立很多留言～）
```sql
create table message (
  id bigint auto_increment primary key comment '獨立編號',
  member_id bigint not null comment '留言者會員編號',
  content varchar(255) not null comment '留言內容',
  time datetime not null default current_timestamp comment '留言時間',
  foreign key(member_id) references member(id)
) character set utf8mb4 collate utf8mb4_0900_ai_ci;

insert into message(member_id, content)
values(1,'test_user_msg1'),
(2,'user01_msg1'),
(1,'test_user_msg2'),
(5,'user04_msg1'),
(3,'user02_msg1'),
(2,'user01_msg2'),
(1,'test_user_msg3'),
(5,'user04_msg2'),
(4,'user03_msg1'),
(1,'test_user_msg4'),
(2,'user01_msg3');

select * from message;
```
#### 取得所有留言 + 留言者會員姓名
```sql
select message.*, member.name from message inner join member on member.id = message.member_id;
```
![message-and-member-name](https://images.plurk.com/6KpsukQ5xhhuOuPuw7rKcl.jpg)
#### 取得 username 是 test 的所有留言 + 留言者會員姓名（先把一個會員的 username 改回 test，不然上面都改成 test2 了）
```sql
update member set username = 'test' where id = 1;

select message.*, member.name from message inner join member on member.id = message.member_id where username = 'test';
```
![avg-follower-count](https://images.plurk.com/57jT4CqeAwC9WBueRLRO9k.jpg)
### mysqldump 筆記（win10）
#### 輸出 data.sql 檔
> 問題：命令提示字元跟 power shell 都不認得 mysql、mysqldump
- 解法1：設定電腦的系統環境變數
- 解法2：power shell cd 移到 mysql exe 檔的所在路徑，在那個路徑下執行指令
> 問題：comment 因為打中文，輸出變亂碼
- 解法：輸出的指令加 `--default-character-set=utf8mb4`
#### 匯入 data.sql 檔（想確認輸出的檔案有沒有問題，所以試了）
> 問題：power shell 顯示 '<' 運算子保留供未來使用。
- 解法：power shell 還不支援 '<'，只好改用命令提示字元
> 問題：ERROR: ASCII '\0' ... Set --binary-mode to 1 if ASCII '\0' is expected.
- 解法1：匯入的指令加 `--binary-mode -o`