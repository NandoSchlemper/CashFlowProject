use actix_web::{web, App, HttpResponse, HttpServer, Responder};

// Handlerr
async fn home() -> impl Responder {
    HttpResponse::Ok().message_body("Hey")
}


// Roteamento
// Define como as requisições são mapeadas p/ handlers especificos com base na URL
// E metodos HTTP
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let bind_address = "127.0.0.1:8080";
    println!("Server instanciado na porta: {}", bind_address);
    HttpServer::new(|| App::new()
            .route("/", web::get().to(home)))
        .bind(bind_address)?
        .run()
        .await
}

// Utilizar Actix-files para handle de arquivos estáticos (HTML + CSS)