use num_bigint::BigUint;
fn main() {
    let mut result = BigUint::from(1u32);
    for i in 2..=100{
        result *= BigUint::from(i as u32);
    }
    println!("100! = {}",result);
}
