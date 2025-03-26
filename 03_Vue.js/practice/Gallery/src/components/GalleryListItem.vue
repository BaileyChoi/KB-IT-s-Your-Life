<script>
export default {
  name: "GalleryListItem",
  props: ["image"],
  inject: ["setSelectedImage"],
};
</script>

<template>
  <li class="gallery-item" @click="setSelectedImage(image)">
    <img :src="image.img" class="item-img" />
    <p>{{ image.title }}</p>
  </li>
</template>

<style>
.gallery-item {
  cursor: pointer;
  text-align: center;
  padding: 10px;
  border: 1px solid gray;
  border-radius: 10px;
  transition: transform 0.2s box-shadow 0.2s;
}

.gallery-item:hover {
  transform: scale(1.05);
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
}

.item-img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 10px;
}
</style>
