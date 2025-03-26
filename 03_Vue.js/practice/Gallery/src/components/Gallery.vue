<script>
import { computed } from "vue";
import GalleryView from "./GalleryView.vue";
import GalleryList from "./GalleryList.vue";

export default {
  name: "Gallery",
  components: { GalleryView, GalleryList },
  data() {
    return {
      images: [
        { id: 1, img: "./pomeranian.jpg", title: "Pomeranian" },
        { id: 2, img: "./poodle.jpg", title: "Poodle" },
        { id: 3, img: "./rottweiler.jpg", title: "Rottweiler" },
        { id: 4, img: "./maltese.jpg", title: "Maltese" },
        { id: 5, img: "./malamute.jpg", title: "Malamute" },
        { id: 6, img: "./beagle.jpg", title: "Beagle" },
        { id: 7, img: "./bulldog.jpg", title: "Bulldog" },
        { id: 8, img: "./retriever.jpg", title: "Retriever" },
      ],
      selectedImage: { id: 1, img: "./pomeranian.jpg", title: "Pomeranian" },
    };
  },
  methods: {
    setSelectedImage(image) {
      this.selectedImage = image;
    },
  },
  provide() {
    return {
      images: this.images,
      selectedImage: computed(() => this.selectedImage),
      setSelectedImage: this.setSelectedImage,
    };
  },
};
</script>

<template>
  <GalleryView />
  <GalleryList />
</template>
