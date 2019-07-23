<template>
  <div class="shadow-card" :class="{'no-margin' : !margin,'no-padding' : !padding}">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    name: 'ShadowCard',
    props: {
      'margin': {
        Boolean,
        default: true
      },
      'padding': {
        Boolean,
        default: true
      }
    }
  }
</script>

<style scoped lang="less">
  .shadow-card {
    box-shadow: @card-shadow;
    background-color: white;
    padding: 12px;
    border-radius: @card-border-radius;
    margin: 8px 4px;
  }

  .no-padding {
    padding: 0 !important;
  }

  .no-margin {
    margin: 0 !important;
  }

  @media screen and (max-width: 768px) {
    .shadow-card {
      padding: 6px 12px;
    }
  }
</style>
