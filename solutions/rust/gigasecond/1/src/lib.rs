use time::PrimitiveDateTime as DateTime;
use time::ext::NumericalDuration;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    let n = i64::pow(10, 9);
    let gigasecond = n.seconds();

    start + gigasecond
}
