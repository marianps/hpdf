var projectConfig = {
  url: {
    data: "https://data." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/v1/query",
    auth: "https://auth." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/v1",
    register: "https://app." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/dregister",
    login: "https://app." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/dlogin",
    filelist: "https://app." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/filelist",
    filestore: "https://filestore." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/v1/file",
    folderUpdate: "https://app." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/fupload2",
    folderList: "https://app." + process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/fldrlist",
    logout: "https://app."+ process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/dlogout",
    createFolder: "https://app."+ process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/fldrcreate",
    useract:  "https://app."+ process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/usract",
    logact: "https://app."+ process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/actvty",
    qaccess: "https://app."+ process.env.REACT_APP_CLUSTER_NAME + ".hasura-app.io/qaccess",

  }
}



const saveOffline = (authToken) => {
  window.localStorage.setItem('authToken', authToken);
}

const getSavedToken = () => {
  return window.localStorage.getItem('authToken');
}

module.exports = {
  projectConfig,
  saveOffline,
  getSavedToken
};
//https://t47d.anthology78.hasura-app.io/dlogin'