import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import PredictComponent from "@/components/PredictComponent";
import LabelledImagesView from "@/views/LabelledImagesView";
import UnlabelledImagesView from "@/views/UnlabelledImagesView";
import {nextTick} from 'vue';

const DEFAULT_TITLE = 'Retinal Predicting and Labelling';

const routes = [
    {
        path: "/",
        name: "Home",
        component: HelloWorld,
    },
    {
        path: "/Predict",
        name: "Predictor",
        component: PredictComponent,
    },
    {
        path: "/Labeling",
        name: "Labeling Images",
        component: UnlabelledImagesView,
    },
    {
        path: "/labelled",
        name: "Labelled Images",
        component: LabelledImagesView,
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
router.afterEach(async (to) => {
    // Use next tick to handle router history correctly
    // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
    await nextTick(() => {
        document.title = to.name || DEFAULT_TITLE;
    });
});
export default router;