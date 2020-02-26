exports.handler = async (event, context) => {
    context.done(null, new Response(200, JSON.stringify({data: "hello world"})));
  };
  
  class Response{
    constructor(statusCode, body){
      this.statusCode = statusCode;
      this.body = body;
      this.headers = {"Access-Control-Allow-Origin" : "*"};
    }
  }