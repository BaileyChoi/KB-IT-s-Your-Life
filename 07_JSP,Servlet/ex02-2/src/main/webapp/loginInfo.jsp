<%--
  Created by IntelliJ IDEA.
  User: student
  Date: 2025-05-29
  Time: 오후 1:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>로그인</title>
</head>
<body>
    <h1>로그인 입력 파라미터 출력</h1>
<%
    String userid = request.getParameter("userid");
    String password = request.getParameter("password");
%>
아이디값: <%= userid %>
비밀번호: <%= password %>
</body>
</html>
