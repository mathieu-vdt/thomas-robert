<script>
export default {
  props: {
    number: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  }
}
</script>
<template>
  <div class="title-style">
    <p class="number">{{ number }}</p>
    <p class="about-me">{{ title }}</p>
    <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="30" height="30" fill="url(#paint0_linear_612_25)" />
      <defs>
        <linearGradient
          id="paint0_linear_612_25"
          x1="15"
          y1="0"
          x2="15"
          y2="30"
          gradientUnits="userSpaceOnUse"
        >
          <stop stop-color="#EC723D" />
          <stop offset="1" stop-color="#f7c7b2" />
        </linearGradient>
      </defs>
    </svg>
  </div>
</template>

<style scoped>
.title-style {
  height: 170px;
  position: relative;
  p {
    &.number {
      color: transparent;
      -webkit-text-stroke: 1px rgb(0, 0, 0);
      font-size: 8em;
      font-weight: 700;
    }

    &.about-me {
      position: absolute;
      font-size: 2em;
      font-weight: 700;
      top: 82px;
      left: 70px;
      background: linear-gradient(270deg, #ec723d, #ff4e00);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }
  svg {
    position: absolute;
    top: 90px;
    left: 30px;
  }
}
</style>
