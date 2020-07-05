#!/usr/bin/env bash

mongoimport --db generators --collection complimentsForMan_phrase --file /opt/data/complimentsForMan_phrase.json
mongoimport --db generators --collection complimentsForMan_word --file /opt/data/complimentsForMan_word.json
mongoimport --db generators --collection complimentsForWoman_phrase --file /opt/data/complimentsForWoman_phrase.json
mongoimport --db generators --collection complimentsForWoman_word --file /opt/data/complimentsForWoman_word.json
mongoimport --db generators --collection facts --file /opt/data/facts.json
mongoimport --db generators --collection jokes --file /opt/data/jokes.json
mongoimport --db generators --collection nameForMan_f --file /opt/data/nameForMan_f.json
mongoimport --db generators --collection nameForMan_i --file /opt/data/nameForMan_i.json
mongoimport --db generators --collection nameForMan_o --file /opt/data/nameForMan_o.json
mongoimport --db generators --collection nameForWoman_f --file /opt/data/nameForWoman_f.json
mongoimport --db generators --collection nameForWoman_i --file /opt/data/nameForWoman_i.json
mongoimport --db generators --collection nameForWoman_o --file /opt/data/nameForWoman_o.json
mongoimport --db generators --collection quotes --file /opt/data/quotes.json

mongoimport --db generators --collection text_prose --file /opt/data/text_prose.json
mongoimport --db generators --collection text_business --file /opt/data/text_business.json
mongoimport --db generators --collection text_science --file /opt/data/text_science.json
mongoimport --db generators --collection text_humor --file /opt/data/text_humor.json
mongoimport --db generators --collection text_home --file /opt/data/text_home.json
mongoimport --db generators --collection text_med --file /opt/data/text_med.json
mongoimport --db generators --collection text_lorem --file /opt/data/text_lorem.json
mongoimport --db generators --collection text_fish --file /opt/data/text_fish.json
