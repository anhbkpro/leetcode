#[derive(Debug)]
enum Cereal {
    Barley, Millet, Rice,
    Rye, Spelt, Wheat,
}

fn main() {
    let mut grains: Vec<Cereal> = vec![];
    grains.push(Cereal::Rice);
    drop(grains);

    println!("{:?}", grains);
}
