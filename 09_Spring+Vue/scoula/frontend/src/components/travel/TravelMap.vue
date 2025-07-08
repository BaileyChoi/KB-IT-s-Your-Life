<script setup>
import { reactive, ref } from "vue";
import { KakaoMap, KakaoMapMarker } from "vue3-kakao-maps";

const props = defineProps({
	title: { type: String, required: true },
	address: { type: String, required: true },
});

// 서울 시청 좌표
const coordinate = reactive({
	lat: 37.566826,
	lng: 126.9786567,
});

const map = ref();

const onLoadKakaoMap = (mapRef) => {
	map.value = mapRef; // 지도 객체
	const geocoder = new kakao.maps.services.Geocoder();

	// 주소로 좌표 검색
	geocoder.addressSearch(props.address, (result, status) => {
		// 정상적으로 검색이 완료됐으면
		if (status == kakao.maps.services.Status.OK) {
			coordinate.lat = result[0].y;
			coordinate.lng = result[0].x;
		}
	});
};

const visibleRef = ref(false); // 초기에 정보창 숨김
const contentRef = ref(props.title);

const onClickKakoMapMarker = () => {
	contentRef.value = `위도: ${parseFloat(coordinate.lat).toFixed(
		2
	)}, 경도: ${parseFloat(coordinate.lng).toFixed(2)}`;
	// visibleRef.value = !visibleRef.value; // 정보창 보이기 토글
	visibleRef.value = true;
};

const onMouseOverKakaoMapMarker = () => {
	contentRef.value = props.title;
	visibleRef.value = true;
};

const onMouseOutKakaoMapMarker = () => {
	visibleRef.value = false;
};
</script>

<template>
	<div><i class="fa-solid fa-map-location-dot"></i> 주소: {{ address }}</div>
	<kakao-map
		:lat="coordinate.lat"
		:lng="coordinate.lng"
		:level="3"
		:draggable="true"
		style="width: 100%"
		@on-load-kakao-map="onLoadKakaoMap"
	>
		<kakao-map-marker
			:lat="coordinate.lat"
			:lng="coordinate.lng"
			:info-window="{ content: contentRef, visible: visibleRef }"
			:clickable="true"
			@on-click-kakao-map-marker="onClickKakoMapMarker"
			@mouse-over-kakao-map-marker="onMouseOverKakaoMapMarker"
			@mouse-out-kakao-map-marker="onMouseOutKakaoMapMarker"
		/>
	</kakao-map>
</template>
