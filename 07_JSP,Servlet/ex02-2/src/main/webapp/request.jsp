<%--
  Created by IntelliJ IDEA.
  User: student
  Date: 2025-05-29
  Time: 오전 11:27
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Request</title>
</head>
<body>
<h1>로그인 입력 화면</h1>
<form action="loginInfo.jsp" method="get">
    <fieldset>
        <legend>로그인 폼</legend>
        <ul style="list-style: none">
            <li>
                <label for="userid">아이디</label>
                <input type="text" name="userid" id="userid">
            </li>
            <li>
                <label for="password">비밀번호</label>
                <input type="password" name="password" id="password">
            </li>
            <li><input type="submit" value="전송"></li>
        </ul>
    </fieldset>
</form>
</body>
</html>
