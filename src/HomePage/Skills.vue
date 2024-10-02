<script lang="ts">
import { defineComponent } from 'vue'
import TitleNumber from '../components/TitleNumber.vue'

export default {
  components: {
    TitleNumber
  },
  data() {
    return {}
  }
}
</script>

<template>
  <div id="skills">
    <div class="skills-text">
      <p class="skills-f">SKILLS</p>
      <p class="skills-b">SKILLS</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#skills {
  margin: 0;

  .skills-text {
    position: relative;
    .skills-f {
      font-size: 8em;
      font-weight: 700;
      background: linear-gradient(80deg, #7ff3d8, #d08ffb);
      background-size: 50% 150%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .skills-b {
      position: absolute;
      font-size: 8em;
      font-weight: 700;
      left: 40px;
      background-size: 50% 150%;
      -webkit-text-stroke: 1px linear-gradient(80deg, #7ff3d8, #d08ffb);
    }
  }
}
</style>
