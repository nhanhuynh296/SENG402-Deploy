import axios from "axios";

let server_url
if (process.env["NODE_ENV"] === "development") {
    server_url = `${process.env.VUE_APP_SERVER_URL}:${process.env.VUE_APP_SERVER_PORT}`
} else if (process.env["NODE_ENV"] === "production") {
    server_url = `${process.env.VUE_APP_SERVER_URL}`
}
export const SERVER_URL = server_url


const axiosInstance = axios.create({
    baseURL: SERVER_URL
});
export default axiosInstance;
