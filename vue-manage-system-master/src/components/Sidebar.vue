<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
        <template  v-if = checknow()>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index">
                        <template #title>
                            <i :class="item.icon"></i>
                            <span>{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-submenu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                            >
                                <template #title>{{ subItem.title }}</template>
                                <el-menu-item
                                    v-for="(threeItem, i) in subItem.subs"
                                    :key="i"
                                    :index="threeItem.index"
                                >{{ threeItem.title }}</el-menu-item>
                            </el-submenu>
                            <el-menu-item
                                v-else
                                :index="subItem.index"
                                :key="subItem.index"
                            >{{ subItem.title }}</el-menu-item>
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <template #title>{{ item.title }}</template>
                    </el-menu-item>
                </template>
            </template>
        </template>

        <template  v-else>
            



        </template> 

        </el-menu>
    </div>
</template>

<script>
// import bus from "../common/bus";
export default {
    data() {
        return {
            items: [
                {
                    icon: "el-icon-lx-home",
                    index: "admininfo",
                    title: "管理员信息"
                },
                {
                    icon: "el-icon-lx-cascades",
                    index: "newclient",
                    title: "用户创建"
                },
                {
                    icon: "el-icon-lx-copy",
                    index: "savenote",
                    title: "储蓄账户创建"
                },
                {
                    icon: "el-icon-lx-calendar",
                    index: "3",
                    title: "储蓄账户管理",
                    subs: [
                        {
                            index: "form",
                            title: "基本表单"
                        },
                        {
                            index: "upload",
                            title: "文件上传"
                        }
                    ]
                },
                {
                    icon: "el-icon-lx-emoji",
                    index: "icon",
                    title: "贷款申请"
                },
                {
                    icon: "el-icon-pie-chart",
                    index: "charts",
                    title: "用户信息查询"
                },
                // {
                //     icon: "el-icon-lx-global",
                //     index: "i18n",
                //     title: "国际化功能"
                // },
                {
                    icon: "el-icon-lx-warn",
                    index: "7",
                    title: "用户账户查询",
                    subs: [
                        {
                            index: "permission",
                            title: "贷款账户查询"
                        },
                        {
                            index: "404",
                            title: "储蓄账户查询"
                        }
                    ]
                }
            ]
        };
    },
    computed: {
        onRoutes() {
            return this.$route.path.replace("/", "");
        },
        collapse(){
            return this.$store.state.collapse
        }
    },

    methods: {
        checknow: function() {
            var res = false;
            const role = localStorage.getItem('user_type');
            if(role === "admin"){
            res = true;
            }
            else res = false;
            return res;
    }

}    
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
