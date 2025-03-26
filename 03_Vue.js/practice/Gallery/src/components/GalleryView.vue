<script>
export default {
  name: "GalleyView",
  inject: ["selectedImage"],
};
</script>

<template>
  <div class="gallery-view">
    <img :src="selectedImage.img" class="view-image" />
    <p>{{ selectedImage.title }}</p>
  </div>
</template>

<style>
.gallery-view {
  text-align: center;
  margin-bottom: 20px;
}
.view-image {
  width: 500px;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
}
</style>
