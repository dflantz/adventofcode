#![feature(string_remove_matches)]

use std::{
    borrow::Borrow,
    cell::RefCell,
    collections::{HashMap, HashSet},
    rc::Rc,
};

struct Fs {
    dirs: Vec<Directory>,
}

impl Fs {
    fn get_dir_sum(&self, index: usize) -> usize {
        let mut sum = 0;
        for i in &self.dirs[index].child_directory_indices {
            sum += self.get_dir_sum(*i)
        }
        let s = sum + self.dirs[index].file_sizes.iter().sum::<usize>();
        println!("sum for {}: {}", &self.dirs[index].dir_name, s);
        return s;
    }
}
struct Directory {
    dir_name: String,
    child_directory_indices: Vec<usize>,
    file_sizes: Vec<usize>,
    index: usize,
    parent_directory_index: Option<usize>,
}

fn main() {
    let mut fs = Fs {
        dirs: vec![Directory {
            dir_name: "/".to_string(),
            child_directory_indices: Vec::new(),
            file_sizes: Vec::new(),
            index: 0,
            parent_directory_index: None,
        }],
    };

    let mut i = 0;

    let mut dir_set: HashSet<&str> = HashSet::new();
    let mut cur_dir = "/".to_string();

    for l in include_str!("../input.txt").lines() {
        let mut words = l.split(" ");
        let s = words.next().unwrap();
        match s {
            "$" => {
                let word = words.next().unwrap();
                match word {
                    "cd" => {
                        let target = words.next().unwrap();
                        match target {
                            ".." => {
                                i = fs.dirs[i].parent_directory_index.unwrap();
                                cur_dir = fs.dirs[i].dir_name.clone();
                            }
                            "/" => {
                                cur_dir = "/".to_string();
                                i = 0;
                            }
                            _ => {
                                cur_dir.push_str(target);
                                i = fs.dirs.iter().position(|d| d.dir_name == cur_dir).unwrap();
                            }
                        }
                    }
                    _ => (),
                }
            }
            "dir" => {
                let mut new_dir = cur_dir.clone();
                new_dir.push_str(words.next().unwrap());
                let d = Directory {
                    dir_name: new_dir,
                    child_directory_indices: Vec::new(),
                    file_sizes: Vec::new(),
                    index: fs.dirs.len(),
                    parent_directory_index: Some(i),
                };
                let len = fs.dirs.len();
                fs.dirs[i].child_directory_indices.push(len);
                fs.dirs.push(d);
            }
            _ => fs.dirs[i].file_sizes.push(s.parse::<usize>().unwrap()),
        };
    }

    // let answer = 0;
    // for i in 0..fs.dirs.len() {
    //     dir_sum = fs.get_dir_sum(i);
    //     if dir_sum > 100000 {}
    // }
    let ans = fs
        .dirs
        .iter()
        .enumerate()
        .map(|(i, _)| fs.get_dir_sum(i))
        .filter(|x| *x <= 100000)
        .sum::<usize>();
    println!("{}", ans);
}
