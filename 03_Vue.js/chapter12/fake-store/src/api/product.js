import axios from "axios";

const BASE = "/api/products";

export const get = async (target, params) => {
  try {
    const response = await axios.get(BASE + target, { params });
    if (response.status === 200) {
      //   console.log(response);
      return response.data;
    }
  } catch (error) {
    console.log("에러 발생 : " + error);
  }
};
export const post = async (target, product) => {
  try {
    const response = await axios.post(BASE + target, product);
    if (response.status === 201) {
      //   console.log(response);
      return response.data;
    }
  } catch (error) {
    console.log("에러 발생 : " + error);
  }
};
export const put = async (target, product) => {
  try {
    const response = await axios.put(BASE + target, product);
    if (response.status === 200) {
      //   console.log(response);
      return response.data;
    }
  } catch (error) {
    console.log("에러 발생 : " + error);
  }
};
export const remove = async (target, params) => {
  try {
    const response = await axios.delete(BASE + target, { params });
    if (response.status === 200) {
      //   console.log(response);
      return response.data;
    }
  } catch (error) {
    console.log("에러 발생 : " + error);
  }
};
