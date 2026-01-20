use std::cmp::Ordering;

struct SegmentTree {
    xs: Vec<i32>,
    n: usize,
    count: Vec<i32>,
    covered: Vec<i32>,
}

impl SegmentTree {
    fn new(xs: Vec<i32>) -> Self {
        let n = xs.len() - 1;
        SegmentTree {
            xs,
            n,
            count: vec![0; 4 * n],
            covered: vec![0; 4 * n],
        }
    }

    fn update(&mut self, ql: i32, qr: i32, val: i32, left: usize, right: usize, pos: usize) {
        if self.xs[right + 1] <= ql || self.xs[left] >= qr {
            return;
        }

        if ql <= self.xs[left] && self.xs[right + 1] <= qr {
            self.count[pos] += val;
        } else {
            let mid = (left + right) / 2;
            self.update(ql, qr, val, left, mid, pos * 2 + 1);
            self.update(ql, qr, val, mid + 1, right, pos * 2 + 2);
        }

        if self.count[pos] > 0 {
            self.covered[pos] = self.xs[right + 1] - self.xs[left];
        } else if left == right {
            self.covered[pos] = 0;
        } else {
            self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2];
        }
    }

    fn query(&self) -> i32 {
        self.covered[0]
    }
}

pub struct Solution;

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut events: Vec<(i32, i32, i32, i32)> = Vec::new();
        let mut xs: Vec<i32> = Vec::new();

        // Build events
        for sq in &squares {
            let (x, y, l) = (sq[0], sq[1], sq[2]);
            events.push((y, 1, x, x + l));
            events.push((y + l, -1, x, x + l));
            xs.push(x);
            xs.push(x + l);
        }

        xs.sort_unstable();
        xs.dedup();

        events.sort_by(|a, b| a.0.cmp(&b.0));

        let mut seg = SegmentTree::new(xs);

        let mut psum: Vec<f64> = Vec::new();
        let mut widths: Vec<f64> = Vec::new();

        let mut total_area = 0.0;
        let mut prev_y = events[0].0;

        // Line sweep
        for &(y, delta, xl, xr) in &events {
            let length = seg.query() as f64;
            total_area += length * (y - prev_y) as f64;

            seg.update(xl, xr, delta, 0, seg.n - 1, 0);

            psum.push(total_area);
            widths.push(seg.query() as f64);

            prev_y = y;
        }

        // Find half-area point
        let target = total_area / 2.0;

        let mut lo = 0usize;
        let mut hi = psum.len();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if psum[mid] >= target {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        let i = lo.saturating_sub(1);
        let area_before = psum[i];
        let width = widths[i];
        let height = events[i].0 as f64;

        height + (target - area_before) / width
    }
}
