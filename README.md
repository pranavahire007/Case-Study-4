# Case-Study-4
# 📚 Library Book Search System Using Hashing
> A simple Python-based Library Book Search System developed using a Hash Table and Separate Chaining to manage and search library books efficiently.

---

## 🎯 Objective
The objective of this case study is to develop a Library Book Search System using the **Hashing technique** in Python. The system stores and manages book information using a hash table and allows users to add, search, delete, and display book records efficiently.

This project demonstrates the use of hash functions and collision resolution techniques to improve the efficiency of searching and managing library records.

---

## 📖 Introduction
A library contains a large number of books, and managing their records manually can be time-consuming. Searching for a particular book among many records may also take considerable time.

Hashing is a data structure technique that helps store and retrieve data efficiently by converting a key into an index using a hash function.

In this project, each book is identified by a unique Book ID. The Book ID is passed through a hash function to calculate the index where the book record will be stored in the hash table.

The system uses **Separate Chaining** to handle collisions. If multiple Book IDs generate the same index, their records are stored together in a list at that index.

This project demonstrates how hashing can be used in a real-world library management application.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Book | Adds a new book with its ID, title, and author. |
| 🔍 Search Book | Searches for a book using its Book ID. |
| ❌ Delete Book | Removes a book record using its ID
