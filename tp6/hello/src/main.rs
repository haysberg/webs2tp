use wsdl::Wsdl;
use rocket::http::{Status, ContentType};

#[macro_use] extern crate rocket;

#[get("/hello/<name>")]
fn hello_name(name: Option<&str>) -> String {
    match name {
        Some(value) => format!("Hello, {}!", value),
        None => format!("Hello, World!")
    }
}

#[get("/hello")]
fn hello() -> String {
    hello_name(Some("World"))
}

#[get("/")]
fn index() -> String {
    format!("Head over to http://localhost:8000/hello/name or /hello?wsdl")
}

#[get("/hello?wsdl")]
fn get_wsdl() -> (Status, (ContentType, String)) {
    (Status::Ok, (ContentType::XML, std::fs::read_to_string("hello.wsdl").unwrap()))
}


fn parse_wsdl() {
    let input = std::fs::read_to_string("hello.wsdl").unwrap();
    let document = roxmltree::Document::parse(&input).unwrap();

    let wsdl = Wsdl::new(&document);
    for service in wsdl.services().unwrap() {
        println!("Service: {}", service.name().unwrap());
    }

    for binding in wsdl.bindings().unwrap() {
        println!(
            "Binding: {} -> {}",
            binding.name().unwrap(),
            binding.port_type().unwrap().name().unwrap()
        );
    }
}

#[launch]
fn rocket() -> _ {
    println!("Reading WSDL...");
    parse_wsdl();

    rocket::build().mount("/", routes![index, hello, hello_name, get_wsdl])
}