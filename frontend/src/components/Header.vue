<template>
    <div id="header">
        <div class="header-container">
            <slot></slot>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'Header',
    mounted () {
    }
  }
</script>

<style scoped lang="less">

    #header {
        position: fixed;
        height: 48px;
        width: 100%;
        top: 0;
        background-color: white;
        color: #000;
        box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);
        z-index: 1;
        @media screen and (max-width: 425px) {
            height: 36px;
        }
    }

    .header-container {
        max-width: @body-max-width;
        height: 100%;
        width: 100%;
        margin: 0 auto;
        padding: 0 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .header-title {
        font-size: 20px;
        cursor: pointer;
    }
</style>
