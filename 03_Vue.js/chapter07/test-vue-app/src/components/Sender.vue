<script>
export default {
	name: "Sender",
	methods: {
		sendMessage() {
			const now = new Date();
			this.emitter.emit(
				"message",
				`${now.getMinutes()}분 ${now.getSeconds()}초에 발신된 메세지`
			);
		},
	},
};
</script>

<template>
	<div style="border: solid 1px orange; margin: 5px; padding: 5px">
		<h2>Sender</h2>
		<button @click="sendMessage">이벤트 발신</button>
	</div>
</template>
