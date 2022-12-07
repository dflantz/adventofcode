use std::collections::HashMap;

struct Directory<'a> {
    child_directories: HashMap<&'a str, Directory<'a>>,
    file_sizes: Vec<usize>,
    parent_directory: Option<&'a Directory<'a>>,
}

fn main() {
    let mut root = Directory {
        child_directories: HashMap::new(),
        file_sizes: Vec::new(),
        parent_directory: None,
    };

    let curr_dir_pointer = &mut root;

    for l in include_str!("../input.txt").lines() {
        let s = l.split(" ").next().unwrap();
        print!("{}: ", s);
        match s {
            "$" => println!("Run command"),
            "dir" => {
                curr_dir_pointer.child_directories.insert(
                    s,
                    Directory {
                        child_directories: HashMap::new(),
                        file_sizes: Vec::new(),
                        parent_directory: None,
                    },
                );
            }
            _ => println!("Add Entry to Dir"),
        };
    }
}
