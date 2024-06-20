use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn home() -> impl Responder {
    HttpResponse::Ok().body("Bruh")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let bind_address = "127.0.0.1:8080";
    HttpServer::new(|| App::new().service(web::scope("/").route("/", web::get().to(home))))
        .bind(bind_address)?
        .run()
        .await
}
