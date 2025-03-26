<script>
import NamedSlotTest from "./components/NamedSlotTest.vue";
import NoSlotTest from "./components/NoSlotTest.vue";
import ScopedSlotTest from "./components/ScopedSlotTest.vue";
import SlotTest from "./components/SlotTest.vue";

export default {
	name: "App",
	components: { NoSlotTest, SlotTest, NamedSlotTest, ScopedSlotTest },
};
</script>

<template>
	<NoSlotTest />
	<SlotTest />
	<NamedSlotTest />
	<ScopedSlotTest />
</template>
