use std::io;
use std::io::prelude::*;

static SCORES: &'static [i32] = &[0, 3, 6];
fn we_play_our(op: char, our: char) -> i32{
    let idx = our as i32 - b'X' as i32;
    let diff = (op as i32 - b'A' as i32 - 2).abs() + 2;
    
    return SCORES[((idx + diff) % 3) as usize];
}

static MOVES: &'static [char] = &['X', 'Y', 'Z'];
fn we_play_given_outcome(op: char, outcome: char) -> char{
    let idx = outcome as i32 - b'X' as i32;
    let diff = op as i32 - b'A' as i32 + 2;

    return MOVES[((idx + diff) % 3) as usize];
}

fn score_move(our_move: char) -> i32{
   return our_move as i32 - b'X' as i32 + 1;
}

fn main() {
    let mut p1: i32 = 0;
    let mut p2: i32 = 0;
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let chars: Vec<char> = line.unwrap().chars().collect();

        p1 += we_play_our(chars[0], chars[2]) + score_move(chars[2]);

        let our_move: char = we_play_given_outcome(chars[0], chars[2]);
        p2 += we_play_our(chars[0], our_move) + score_move(our_move);
    }
    println!("{}", p1);
    println!("{}", p2);
}