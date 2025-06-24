<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://www.springframework.org/security/tags" prefix="sec" %>
<html lang="ko">
<head>
    <title>Title</title>
</head>
<body>
<h1>Welcome!</h1>

<sec:authorize access="isAnonymous()"> <!-- 로그인 안한 경우-->
    <a href="/security/login">로그인</a>
</sec:authorize>

<sec:authorize access="isAuthenticated()"> <!-- 로그인 한 경우-->
    <sec:authentication property="principal.username"/>
    <form action="/security/logout" method="post">
        <input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}"/>
        <input type="submit" value="로그아웃"/>
    </form>
</sec:authorize>
</body>
</html>
