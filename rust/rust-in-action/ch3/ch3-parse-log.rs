#[derive(Debug)]
enum Event {
    Update,
    Delete,
    Unknown,
}

type Message = String;

fn parse_log(line: &str) -> (Event, Message) {
    let parts: Vec<_> = line.splitn(2, ' ').collect(); // collect() consumes an iterator from line.splitn() and returns Vec<T>.
    if parts.len() != 2 {
        return (Event::Unknown, line.to_string());
    }
    let event = match parts[0] {
        "UPDATE" => Event::Update,
        "DELETE" => Event::Delete,
        _ => Event::Unknown,
    };
    let message = parts[1].to_string();
    (event, message)
}

fn main() {
    let log_lines = vec![
        "UPDATE 234:LS/32231 {\"price\": 31.00} -> {\"price\": 40.00}",
        "DELETE 342:LO/22111",
        "BEGIN Transaction XK342",
    ];

    for line in log_lines {
        let (event, message) = parse_log(line);
        println!("Event: {:?}, Message: {}", event, message);
    }
}
