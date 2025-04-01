<script setup>
import BaseAlert from "./UI/BaseAlert.vue";
import BaseBadge from "./UI/BaseBadge.vue";
import BaseButton from "./UI/BaseButton.vue";
</script>

<template>
	<!-- 그리드 컨테이너 -->
	<main class="component-grid">
		<!-- 컴포넌트 그룹 (그리드 아이템) -->
		<section class="component-card">
			<h2>버튼</h2>
			<BaseButton variant="primary">Primary</BaseButton>
			<BaseButton variant="outline">Outline</BaseButton>
			<BaseButton variant="pill">Pill</BaseButton>
		</section>

		<!-- 알림창 -->
		<section class="component-card">
			<h2>알림창</h2>
			<BaseAlert variant="success">Success</BaseAlert>
			<BaseAlert variant="warning">Warning</BaseAlert>
			<BaseAlert variant="error">Error</BaseAlert>
		</section>

		<!-- 뱃지 -->
		<section class="component-card">
			<h2>뱃지</h2>
			<BaseBadge variant="success">Success</BaseBadge>
			<BaseBadge variant="number">9</BaseBadge>
		</section>
	</main>
</template>

<style scoped></style>
