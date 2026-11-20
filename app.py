# import streamlit as st
# import html

# # ==========================================
# # 1. PAGE CONFIGURATION
# # ==========================================

# st.set_page_config(
#     page_title="Library Management System",
#     page_icon="📚",
#     layout="wide"
# )

# # ==========================================
# # 2. CUSTOM HTML AND CSS DESIGN
# # ==========================================

# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(135deg, #0f172a, #172554, #1e293b);
#     color: white;
# }

# .main .block-container {
#     padding-top: 2rem;
#     padding-bottom: 3rem;
#     max-width: 1200px;
# }

# .hero {
#     background: linear-gradient(120deg, #2563eb, #7c3aed);
#     padding: 35px;
#     border-radius: 20px;
#     text-align: center;
#     margin-bottom: 25px;
#     box-shadow: 0 10px 30px rgba(0,0,0,0.3);
# }

# .hero h1 {
#     color: white;
#     font-size: 38px;
#     margin-bottom: 8px;
# }

# .hero p {
#     color: #e0e7ff;
#     font-size: 16px;
# }

# .stat-card {
#     background: #1e293b;
#     border: 1px solid #334155;
#     padding: 22px;
#     border-radius: 15px;
#     text-align: center;
#     margin-bottom: 15px;
# }

# .stat-card h2 {
#     color: #60a5fa;
#     font-size: 32px;
#     margin: 5px;
# }

# .stat-card p {
#     color: #cbd5e1;
#     margin: 0;
# }

# .book-card {
#     background: linear-gradient(145deg, #1e293b, #26364e);
#     border: 1px solid #475569;
#     border-radius: 15px;
#     padding: 20px;
#     margin-bottom: 14px;
#     min-height: 170px;
# }

# .book-card h3 {
#     color: #93c5fd;
#     margin-bottom: 10px;
# }

# .book-card p {
#     color: #e2e8f0;
#     margin: 6px 0;
# }

# .available {
#     color: #4ade80;
#     font-weight: bold;
# }

# .issued {
#     color: #fbbf24;
#     font-weight: bold;
# }

# .section-title {
#     color: #93c5fd;
#     font-size: 25px;
#     font-weight: bold;
#     margin-top: 25px;
#     margin-bottom: 15px;
# }

# div.stButton > button {
#     background: linear-gradient(90deg, #2563eb, #7c3aed);
#     color: white;
#     border: none;
#     border-radius: 10px;
#     padding: 10px 20px;
#     font-weight: bold;
#     width: 100%;
# }

# div.stButton > button:hover {
#     background: #4f46e5;
#     color: white;
#     border: none;
# }

# [data-testid="stSidebar"] {
#     background-color: #111827;
# }

# label, .stMarkdown, p {
#     color: #e2e8f0;
# }

# </style>
# """, unsafe_allow_html=True)


# # ==========================================
# # 3. BOOK CLASS
# # ==========================================

# class Book:

#     def _init_(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.__available = True

#     @property
#     def available(self):
#         return self.__available

#     def issue(self):
#         if self.__available:
#             self.__available = False
#             return True
#         return False

#     def return_book(self):
#         if not self.__available:
#             self.__available = True
#             return True
#         return False

#     def _str_(self):
#         status = "Available" if self.__available else "Issued"

#         return (
#             f"Title: {self.title} | "
#             f"Author: {self.author} | "
#             f"ISBN: {self.isbn} | "
#             f"Status: {status}"
#         )


# # ==========================================
# # 4. MEMBER CLASS
# # ==========================================

# class Member:

#     def _init_(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.__borrowed_books = []

#     def issue_book(self, book):

#         if book in self.__borrowed_books:
#             return "This book is already borrowed by this member."

#         if book.issue():
#             self.__borrowed_books.append(book)
#             return f"{book.title} issued successfully to {self.name}!"

#         return f"Sorry! {book.title} is not available."

#     def return_book(self, book):

#         if book not in self.__borrowed_books:
#             return "This member has not borrowed this book."

#         self.__borrowed_books.remove(book)
#         book.return_book()

#         return f"{book.title} returned successfully by {self.name}!"

#     def get_borrowed_books(self):
#         return self.__borrowed_books.copy()

#     def _len_(self):
#         return len(self.__borrowed_books)

#     def _str_(self):
#         return (
#             f"Member: {self.name} | "
#             f"ID: {self.member_id} | "
#             f"Borrowed Books: {len(self)}"
#         )


# # ==========================================
# # 5. LIBRARY CLASS (COMPOSITION)
# # ==========================================

# class Library:

#     def _init_(self, name):
#         self.name = name
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)

#     def add_member(self, member):
#         self.members.append(member)

#     def find_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 return book
#         return None


# # ==========================================
# # 6. CREATE SAMPLE DATA
# # ==========================================

# if "library" not in st.session_state:

#     library = Library("Smart Library")

#     sample_books = [
#         Book("Python Programming", "John Zelle", "101"),
#         Book("Clean Code", "Robert Martin", "102"),
#         Book("The Alchemist", "Paulo Coelho", "103"),
#         Book("Atomic Habits", "James Clear", "104"),
#         Book("Rich Dad Poor Dad", "Robert Kiyosaki", "105")
#     ]

#     for book in sample_books:
#         library.add_book(book)

#     member1 = Member("Nivetha", "M001")
#     member2 = Member("Arun", "M002")

#     library.add_member(member1)
#     library.add_member(member2)

#     st.session_state.library = library


# library = st.session_state.library


# # ==========================================
# # 7. DASHBOARD HEADER
# # ==========================================

# st.markdown("""
# <div class="hero">
#     <h1>📚 SMART LIBRARY</h1>
#     <p>Library Management System | Python OOP Project</p>
#     <p>Manage Books • Members • Issue • Return</p>
# </div>
# """, unsafe_allow_html=True)


# # ==========================================
# # 8. DASHBOARD STATISTICS
# # ==========================================

# total_books = len(library.books)

# available_books = sum(
#     1 for book in library.books if book.available
# )

# issued_books = total_books - available_books

# total_members = len(library.members)

# c1, c2, c3, c4 = st.columns(4)

# with c1:
#     st.markdown(f"""
#     <div class="stat-card">
#         <h2>{total_books}</h2>
#         <p>📚 Total Books</p>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown(f"""
#     <div class="stat-card">
#         <h2>{available_books}</h2>
#         <p>✅ Available Books</p>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown(f"""
#     <div class="stat-card">
#         <h2>{issued_books}</h2>
#         <p>📖 Issued Books</p>
#     </div>
#     """, unsafe_allow_html=True)

# with c4:
#     st.markdown(f"""
#     <div class="stat-card">
#         <h2>{total_members}</h2>
#         <p>👥 Members</p>
#     </div>
#     """, unsafe_allow_html=True)


# # ==========================================
# # 9. SIDEBAR NAVIGATION
# # ==========================================

# st.sidebar.title("📚 Library Menu")

# menu = st.sidebar.radio(
#     "Choose an Option",
#     [
#         "Dashboard",
#         "View Books",
#         "Issue Book",
#         "Return Book",
#         "Members"
#     ]
# )

# st.sidebar.markdown("---")
# st.sidebar.info("Smart Library Management System")


# # ==========================================
# # 10. DASHBOARD PAGE
# # ==========================================

# if menu == "Dashboard":

#     st.markdown(
#         '<div class="section-title">Welcome to Smart Library 👋</div>',
#         unsafe_allow_html=True
#     )

#     st.write(
#         "Manage your library easily with this Python OOP application."
#     )

#     st.success("Library system is running successfully!")

#     st.markdown("### ✨ Project Highlights")

#     st.write("✔️ Book and Member classes")
#     st.write("✔️ Encapsulation using private attributes")
#     st.write("✔️ Composition using Library class")
#     st.write("✔️ Special methods: _str() and __len_()")
#     st.write("✔️ Book issue and return validation")


# # ==========================================
# # 11. VIEW BOOKS PAGE
# # ==========================================

# elif menu == "View Books":

#     st.markdown(
#         '<div class="section-title">📖 Book Collection</div>',
#         unsafe_allow_html=True
#     )

#     for book in library.books:

#         status = (
#             '<span class="available">● Available</span>'
#             if book.available
#             else '<span class="issued">● Issued</span>'
#         )

#         st.markdown(f"""
#         <div class="book-card">
#             <h3>📘 {html.escape(book.title)}</h3>
#             <p>✍️ Author: {html.escape(book.author)}</p>
#             <p>🔖 ISBN: {html.escape(book.isbn)}</p>
#             <p>Status: {status}</p>
#         </div>
#         """, unsafe_allow_html=True)


# # ==========================================
# # 12. ISSUE BOOK PAGE
# # ==========================================

# elif menu == "Issue Book":

#     st.markdown(
#         '<div class="section-title">📤 Issue a Book</div>',
#         unsafe_allow_html=True
#     )

#     member = st.selectbox(
#         "Select Member",
#         library.members,
#         format_func=lambda m: m.name
#     )

#     available = [
#         book for book in library.books if book.available
#     ]

#     if available:

#         selected_book = st.selectbox(
#             "Select Book",
#             available,
#             format_func=lambda b: b.title
#         )

#         if st.button("🚀 Issue Book"):

#             message = member.issue_book(selected_book)

#             st.success(message)
#             st.rerun()

#     else:
#         st.warning("No books are currently available!")


# # ==========================================
# # 13. RETURN BOOK PAGE
# # ==========================================

# elif menu == "Return Book":

#     st.markdown(
#         '<div class="section-title">📥 Return a Book</div>',
#         unsafe_allow_html=True
#     )

#     member = st.selectbox(
#         "Select Member",
#         library.members,
#         format_func=lambda m: m.name,
#         key="return_member"
#     )

#     borrowed = member.get_borrowed_books()

#     if borrowed:

#         selected_book = st.selectbox(
#             "Select Borrowed Book",
#             borrowed,
#             format_func=lambda b: b.title
#         )

#         if st.button("↩️ Return Book"):

#             message = member.return_book(selected_book)

#             st.success(message)
#             st.rerun()

#     else:
#         st.info("This member has not borrowed any books.")


# # ==========================================
# # 14. MEMBERS PAGE
# # ==========================================

# elif menu == "Members":

#     st.markdown(
#         '<div class="section-title">👥 Library Members</div>',
#         unsafe_allow_html=True
#     )

#     for member in library.members:

#         st.markdown(f"""
#         <div class="book-card">
#             <h3>👤 {html.escape(member.name)}</h3>
#             <p>Member ID: {html.escape(member.member_id)}</p>
#             <p>Borrowed Books: {len(member)}</p>
#         </div>
#         """, unsafe_allow_html=True)

#         with st.expander(f"View {member.name}'s Borrowed Books"):

#             books = member.get_borrowed_books()

#             if books:
#                 for book in books:
#                     st.write("📘", book.title)
#             else:
#                 st.write("No borrowed books.")


# # ==========================================
# # 15. FOOTER
# # ==========================================

# st.markdown("---")

# st.markdown("""
# <div style="text-align:center; padding:15px;">
#     <p style="color:#93c5fd;">
#         📚 Smart Library Management System
#     </p>
#     <p style="color:#94a3b8;">
#         Developed using Python | OOP | Streamlit | HTML | CSS
#     </p>
# </div>
# """, unsafe_allow_html=True)














































import streamlit as st
import html

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

# ==========================================
# 2. CUSTOM HTML AND CSS DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #172554, #1e293b);
    color: white;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.hero {
    background: linear-gradient(120deg, #2563eb, #7c3aed);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    color: #e0e7ff;
    font-size: 16px;
}

.stat-card {
    background: #1e293b;
    border: 1px solid #334155;
    padding: 22px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 15px;
}

.stat-card h2 {
    color: #60a5fa;
    font-size: 32px;
    margin: 5px;
}

.stat-card p {
    color: #cbd5e1;
    margin: 0;
}

.book-card {
    background: linear-gradient(145deg, #1e293b, #26364e);
    border: 1px solid #475569;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 14px;
    min-height: 170px;
}

.book-card h3 {
    color: #93c5fd;
    margin-bottom: 10px;
}

.book-card p {
    color: #e2e8f0;
    margin: 6px 0;
}

.available {
    color: #4ade80;
    font-weight: bold;
}

.issued {
    color: #fbbf24;
    font-weight: bold;
}

.section-title {
    color: #93c5fd;
    font-size: 25px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 15px;
}

div.stButton > button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    background: #4f46e5;
    color: white;
    border: none;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

label, .stMarkdown, p {
    color: #e2e8f0;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. BOOK CLASS
# ==========================================

class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True

    @property
    def available(self):
        return self.__available

    def issue(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        if not self.__available:
            self.__available = True
            return True
        return False

    def __str__(self):
        status = "Available" if self.__available else "Issued"
        return (
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"ISBN: {self.isbn} | "
            f"Status: {status}"
        )

# ==========================================
# 4. MEMBER CLASS
# ==========================================

class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []

    def issue_book(self, book):
        if book in self.__borrowed_books:
            return "This book is already borrowed by this member."

        if book.issue():
            self.__borrowed_books.append(book)
            return f"{book.title} issued successfully to {self.name}!"

        return f"Sorry! {book.title} is not available."

    def return_book(self, book):
        if book not in self.__borrowed_books:
            return "This member has not borrowed this book."

        self.__borrowed_books.remove(book)
        book.return_book()
        return f"{book.title} returned successfully by {self.name}!"

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()

    def __len__(self):
        return len(self.__borrowed_books)

    def __str__(self):
        return (
            f"Member: {self.name} | "
            f"ID: {self.member_id} | "
            f"Borrowed Books: {len(self)}"
        )

# ==========================================
# 5. LIBRARY CLASS (COMPOSITION)
# ==========================================

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# ==========================================
# 6. CREATE SAMPLE DATA
# ==========================================

if "library" not in st.session_state:

    library = Library("Smart Library")

    sample_books = [
        Book("Python Programming", "John Zelle", "101"),
        Book("Clean Code", "Robert Martin", "102"),
        Book("The Alchemist", "Paulo Coelho", "103"),
        Book("Atomic Habits", "James Clear", "104"),
        Book("Rich Dad Poor Dad", "Robert Kiyosaki", "105")
    ]

    for book in sample_books:
        library.add_book(book)

    member1 = Member("Nivetha", "M001")
    member2 = Member("Arun", "M002")

    library.add_member(member1)
    library.add_member(member2)

    st.session_state.library = library

library = st.session_state.library

# ==========================================
# 7. DASHBOARD HEADER
# ==========================================

st.markdown("""
<div class="hero">
    <h1>📚 SMART LIBRARY</h1>
    <p>Library Management System | Python OOP Project</p>
    <p>Manage Books • Members • Issue • Return</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 8. DASHBOARD STATISTICS
# ==========================================

total_books = len(library.books)

available_books = sum(
    1 for book in library.books if book.available
)

issued_books = total_books - available_books

total_members = len(library.members)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="stat-card">
        <h2>{total_books}</h2>
        <p>📚 Total Books</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="stat-card">
        <h2>{available_books}</h2>
        <p>✅ Available Books</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="stat-card">
        <h2>{issued_books}</h2>
        <p>📖 Issued Books</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="stat-card">
        <h2>{total_members}</h2>
        <p>👥 Members</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 9. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("📚 Library Menu")

menu = st.sidebar.radio(
    "Choose an Option",
    [
        "Dashboard",
        "View Books",
        "Issue Book",
        "Return Book",
        "Members"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Smart Library Management System")

# ==========================================
# 10. DASHBOARD PAGE
# ==========================================

if menu == "Dashboard":

    st.markdown(
        '<div class="section-title">Welcome to Smart Library 👋</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Manage your library easily with this Python OOP application."
    )

    st.success("Library system is running successfully!")

    st.markdown("### ✨ Project Highlights")

    st.write("✔️ Book and Member classes")
    st.write("✔️ Encapsulation using private attributes")
    st.write("✔️ Composition using Library class")
    st.write("✔️ Special methods: __str__() and __len__()")
    st.write("✔️ Book issue and return validation")

# ==========================================
# 11. VIEW BOOKS PAGE
# ==========================================

elif menu == "View Books":

    st.markdown(
        '<div class="section-title">📖 Book Collection</div>',
        unsafe_allow_html=True
    )

    for book in library.books:

        status = (
            '<span class="available">● Available</span>'
            if book.available
            else '<span class="issued">● Issued</span>'
        )

        st.markdown(f"""
        <div class="book-card">
            <h3>📘 {html.escape(book.title)}</h3>
            <p>✍️ Author: {html.escape(book.author)}</p>
            <p>🔖 ISBN: {html.escape(book.isbn)}</p>
            <p>Status: {status}</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 12. ISSUE BOOK PAGE
# ==========================================

elif menu == "Issue Book":

    st.markdown(
        '<div class="section-title">📤 Issue a Book</div>',
        unsafe_allow_html=True
    )

    member = st.selectbox(
        "Select Member",
        library.members,
        format_func=lambda m: m.name
    )

    available = [
        book for book in library.books if book.available
    ]

    if available:

        selected_book = st.selectbox(
            "Select Book",
            available,
            format_func=lambda b: b.title
        )

        if st.button("🚀 Issue Book"):
            message = member.issue_book(selected_book)
            st.success(message)
            st.rerun()

    else:
        st.warning("No books are currently available!")

# ==========================================
# 13. RETURN BOOK PAGE
# ==========================================

elif menu == "Return Book":

    st.markdown(
        '<div class="section-title">📥 Return a Book</div>',
        unsafe_allow_html=True
    )

    member = st.selectbox(
        "Select Member",
        library.members,
        format_func=lambda m: m.name,
        key="return_member"
    )

    borrowed = member.get_borrowed_books()

    if borrowed:

        selected_book = st.selectbox(
            "Select Borrowed Book",
            borrowed,
            format_func=lambda b: b.title
        )

        if st.button("↩️ Return Book"):
            message = member.return_book(selected_book)
            st.success(message)
            st.rerun()

    else:
        st.info("This member has not borrowed any books.")

# ==========================================
# 14. MEMBERS PAGE
# ==========================================

elif menu == "Members":

    st.markdown(
        '<div class="section-title">👥 Library Members</div>',
        unsafe_allow_html=True
    )

    for member in library.members:

        st.markdown(f"""
        <div class="book-card">
            <h3>👤 {html.escape(member.name)}</h3>
            <p>Member ID: {html.escape(member.member_id)}</p>
            <p>Borrowed Books: {len(member)}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"View {member.name}'s Borrowed Books"):

            books = member.get_borrowed_books()

            if books:
                for book in books:
                    st.write("📘", book.title)
            else:
                st.write("No borrowed books.")

# ==========================================
# 15. FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:15px;">
    <p style="color:#93c5fd;">
        📚 Smart Library Management System
    </p>
    <p style="color:#94a3b8;">
        Developed using Python | OOP | Streamlit | HTML | CSS
    </p>
</div>
""", unsafe_allow_html=True)