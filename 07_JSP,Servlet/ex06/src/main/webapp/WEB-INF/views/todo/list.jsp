<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h1>Todo 목록 보기</h1>
    <div>
        [<c:forEach var="todo" items="${todoList}" varStatus="status">
            ${todo}<c:if test="${!status.last}">,</c:if>
        </c:forEach>]
        <a href="view">상세보기</a>
    </div>
    <div>
        <a href="create">New Todo</a>
    </div>
</body>
</html>
