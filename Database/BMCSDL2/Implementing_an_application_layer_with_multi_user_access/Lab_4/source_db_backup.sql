--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Ubuntu 16.4-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.4 (Ubuntu 16.4-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: coffee_shop_schema; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA coffee_shop_schema;


ALTER SCHEMA coffee_shop_schema OWNER TO postgres;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA coffee_shop_schema;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: logging(); Type: FUNCTION; Schema: coffee_shop_schema; Owner: postgres
--

CREATE FUNCTION coffee_shop_schema.logging() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('D', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('U', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('I', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;    
END;
$$;


ALTER FUNCTION coffee_shop_schema.logging() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bill; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.bill (
    bill_id integer NOT NULL,
    amount numeric(10,2) NOT NULL,
    payment character varying(50) NOT NULL,
    order_id integer
);


ALTER TABLE coffee_shop_schema.bill OWNER TO postgres;

--
-- Name: bill_bill_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.bill_bill_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.bill_bill_id_seq OWNER TO postgres;

--
-- Name: bill_bill_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.bill_bill_id_seq OWNED BY coffee_shop_schema.bill.bill_id;


--
-- Name: customer; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.customer (
    customer_id integer NOT NULL,
    name character varying(100) NOT NULL,
    phone_number character varying(13),
    email character varying(100)
);


ALTER TABLE coffee_shop_schema.customer OWNER TO postgres;

--
-- Name: customer_customer_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.customer_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.customer_customer_id_seq OWNER TO postgres;

--
-- Name: customer_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.customer_customer_id_seq OWNED BY coffee_shop_schema.customer.customer_id;


--
-- Name: orders; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.orders (
    order_id integer NOT NULL,
    order_date date NOT NULL,
    total_amount numeric(10,2) NOT NULL,
    employee_id integer,
    customer_id integer
);


ALTER TABLE coffee_shop_schema.orders OWNER TO postgres;

--
-- Name: customer_order_view; Type: VIEW; Schema: coffee_shop_schema; Owner: postgres
--

CREATE VIEW coffee_shop_schema.customer_order_view AS
 SELECT c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    o.total_amount,
    b.bill_id,
    b.amount AS bill_amount,
    b.payment
   FROM ((coffee_shop_schema.customer c
     JOIN coffee_shop_schema.orders o ON ((c.customer_id = o.customer_id)))
     JOIN coffee_shop_schema.bill b ON ((o.order_id = b.order_id)));


ALTER VIEW coffee_shop_schema.customer_order_view OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.employee (
    employee_id integer NOT NULL,
    name character varying(100) NOT NULL,
    "position" character varying(50) NOT NULL,
    phone_number character varying(13),
    email character varying(100)
);


ALTER TABLE coffee_shop_schema.employee OWNER TO postgres;

--
-- Name: employee_employee_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.employee_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.employee_employee_id_seq OWNER TO postgres;

--
-- Name: employee_employee_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.employee_employee_id_seq OWNED BY coffee_shop_schema.employee.employee_id;


--
-- Name: main_log; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.main_log (
    log_id integer NOT NULL,
    operation_type text,
    operation_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    user_operator text,
    changed_data json
);


ALTER TABLE coffee_shop_schema.main_log OWNER TO postgres;

--
-- Name: main_log_log_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.main_log_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.main_log_log_id_seq OWNER TO postgres;

--
-- Name: main_log_log_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.main_log_log_id_seq OWNED BY coffee_shop_schema.main_log.log_id;


--
-- Name: order_product; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.order_product (
    order_id integer,
    product_id integer
);


ALTER TABLE coffee_shop_schema.order_product OWNER TO postgres;

--
-- Name: orders_oder_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.orders_oder_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.orders_oder_id_seq OWNER TO postgres;

--
-- Name: orders_oder_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.orders_oder_id_seq OWNED BY coffee_shop_schema.orders.order_id;


--
-- Name: product; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.product (
    product_id integer NOT NULL,
    product_category_name character varying(100) NOT NULL,
    price numeric(10,2) NOT NULL,
    warehouse_id integer
);


ALTER TABLE coffee_shop_schema.product OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.product_product_id_seq OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.product_product_id_seq OWNED BY coffee_shop_schema.product.product_id;


--
-- Name: sales_employee_view; Type: VIEW; Schema: coffee_shop_schema; Owner: postgres
--

CREATE VIEW coffee_shop_schema.sales_employee_view AS
 SELECT e.employee_id,
    e.name AS employee_name,
    o.order_id,
    o.order_date,
    o.total_amount,
    c.customer_id,
    c.name AS customer_name,
    c.phone_number AS customer_phone,
    c.email AS customer_mail
   FROM ((coffee_shop_schema.employee e
     JOIN coffee_shop_schema.orders o ON ((e.employee_id = o.employee_id)))
     JOIN coffee_shop_schema.customer c ON ((o.customer_id = c.customer_id)));


ALTER VIEW coffee_shop_schema.sales_employee_view OWNER TO postgres;

--
-- Name: secret_data; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.secret_data (
    id integer NOT NULL,
    username text,
    secret_token text
);


ALTER TABLE coffee_shop_schema.secret_data OWNER TO postgres;

--
-- Name: secret_data_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.secret_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.secret_data_id_seq OWNER TO postgres;

--
-- Name: secret_data_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.secret_data_id_seq OWNED BY coffee_shop_schema.secret_data.id;


--
-- Name: supplier; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.supplier (
    supplier_id integer NOT NULL,
    name character varying(100) NOT NULL,
    address character varying(255),
    phone_number character varying(13),
    email character varying(100)
);


ALTER TABLE coffee_shop_schema.supplier OWNER TO postgres;

--
-- Name: supplier_product; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.supplier_product (
    supplier_id integer,
    product_id integer
);


ALTER TABLE coffee_shop_schema.supplier_product OWNER TO postgres;

--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.supplier_supplier_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.supplier_supplier_id_seq OWNER TO postgres;

--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.supplier_supplier_id_seq OWNED BY coffee_shop_schema.supplier.supplier_id;


--
-- Name: warehouse; Type: TABLE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TABLE coffee_shop_schema.warehouse (
    warehouse_id integer NOT NULL,
    address character varying(100) NOT NULL,
    status character varying(50),
    employee_id integer
);


ALTER TABLE coffee_shop_schema.warehouse OWNER TO postgres;

--
-- Name: warehouse_manager_view; Type: VIEW; Schema: coffee_shop_schema; Owner: postgres
--

CREATE VIEW coffee_shop_schema.warehouse_manager_view AS
 SELECT w.warehouse_id,
    w.address AS warehouse_address,
    w.status AS warehouse_status,
    p.product_id,
    p.product_category_name,
    p.price
   FROM (coffee_shop_schema.warehouse w
     JOIN coffee_shop_schema.product p ON ((w.warehouse_id = p.warehouse_id)));


ALTER VIEW coffee_shop_schema.warehouse_manager_view OWNER TO postgres;

--
-- Name: warehouse_warehouse_id_seq; Type: SEQUENCE; Schema: coffee_shop_schema; Owner: postgres
--

CREATE SEQUENCE coffee_shop_schema.warehouse_warehouse_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE coffee_shop_schema.warehouse_warehouse_id_seq OWNER TO postgres;

--
-- Name: warehouse_warehouse_id_seq; Type: SEQUENCE OWNED BY; Schema: coffee_shop_schema; Owner: postgres
--

ALTER SEQUENCE coffee_shop_schema.warehouse_warehouse_id_seq OWNED BY coffee_shop_schema.warehouse.warehouse_id;


--
-- Name: bill bill_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.bill ALTER COLUMN bill_id SET DEFAULT nextval('coffee_shop_schema.bill_bill_id_seq'::regclass);


--
-- Name: customer customer_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.customer ALTER COLUMN customer_id SET DEFAULT nextval('coffee_shop_schema.customer_customer_id_seq'::regclass);


--
-- Name: employee employee_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.employee ALTER COLUMN employee_id SET DEFAULT nextval('coffee_shop_schema.employee_employee_id_seq'::regclass);


--
-- Name: main_log log_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.main_log ALTER COLUMN log_id SET DEFAULT nextval('coffee_shop_schema.main_log_log_id_seq'::regclass);


--
-- Name: orders order_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders ALTER COLUMN order_id SET DEFAULT nextval('coffee_shop_schema.orders_oder_id_seq'::regclass);


--
-- Name: product product_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.product ALTER COLUMN product_id SET DEFAULT nextval('coffee_shop_schema.product_product_id_seq'::regclass);


--
-- Name: secret_data id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.secret_data ALTER COLUMN id SET DEFAULT nextval('coffee_shop_schema.secret_data_id_seq'::regclass);


--
-- Name: supplier supplier_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier ALTER COLUMN supplier_id SET DEFAULT nextval('coffee_shop_schema.supplier_supplier_id_seq'::regclass);


--
-- Name: warehouse warehouse_id; Type: DEFAULT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.warehouse ALTER COLUMN warehouse_id SET DEFAULT nextval('coffee_shop_schema.warehouse_warehouse_id_seq'::regclass);


--
-- Data for Name: bill; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.bill (bill_id, amount, payment, order_id) FROM stdin;
1	150000.00	Cash	1
2	599999.00	Bank Transfer	2
3	50000.00	Cash	3
4	20000.00	Online Payment	3
5	6699999.00	Cash	4
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.customer (customer_id, name, phone_number, email) FROM stdin;
1	Alex	93842727543	alex8888@mail.ru
2	Tom	82736464383	tomi7749@mail.ru
3	Anton	827364646737	ton@mail.ru
4	Karababy	8283747654	baby@mail.ru
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.employee (employee_id, name, "position", phone_number, email) FROM stdin;
1	Nguyen Van A	supervisor	9312828535	nguyenvana123@gmail.com
2	Nguyen Thi B	salesperson	92537563834	nb4214@gmail.com
3	Artom	salesperson	27582473683	artom33@mail.ru
4	Irina	salesperson	8925748253	irina8386@mail.ru
5	Tran	salesperson	92846363583	trantran4953@gmail.com
\.


--
-- Data for Name: main_log; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.main_log (log_id, operation_type, operation_date, user_operator, changed_data) FROM stdin;
1	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
2	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
3	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
4	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
5	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
6	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
7	I	2024-10-26 22:14:47.801626	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
8	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
9	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
10	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
11	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
12	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
13	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
14	U	2024-10-26 22:16:57.623706	postgres	{"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
15	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
16	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
17	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
18	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
19	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
20	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
21	D	2024-10-26 22:17:26.847963	postgres	{"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
\.


--
-- Data for Name: order_product; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.order_product (order_id, product_id) FROM stdin;
1	1
2	2
3	3
4	4
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.orders (order_id, order_date, total_amount, employee_id, customer_id) FROM stdin;
1	2024-10-12	150000.00	2	1
2	2024-10-13	599999.00	2	2
3	2024-10-13	70000.00	3	3
4	2024-10-20	6699999.00	4	4
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.product (product_id, product_category_name, price, warehouse_id) FROM stdin;
1	Arabica	100000.00	1
2	Robusta	90000.00	2
3	Bourbon	96000.00	3
4	Typica	95000.00	4
\.


--
-- Data for Name: secret_data; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.secret_data (id, username, secret_token) FROM stdin;
1	Chu	\\xc30d04070302cbda441b01d7b95274d23a0167245609f84edb96a65edbde2c8b5689019035e368e08cf678485dffc70a65a79480d94e9f8b21af40531c9ce1a89ca09596e9f547218265ef
2	postgres	\\xc30d04070302571df6bfa22c5a2064d23f01406b15d947d495bc01aeb175c38236d0b2cb584474597a12109270332cc8686d8ada1e339139e6ee48af356ada4be450c8e76f019f4d9ce3a60ea7b153d5
\.


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.supplier (supplier_id, name, address, phone_number, email) FROM stdin;
1	Trung Nguyen Coffee	Dalat city	03873532753	trungnguyencoffee@gmail.com
2	King Coffee	Ho Chi Minh city	0385636282	kingcoffee@gmail.com
3	G7 Coffee	Ha Noi	92834772843	g7coffee@gmail.com
\.


--
-- Data for Name: supplier_product; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.supplier_product (supplier_id, product_id) FROM stdin;
1	1
1	2
2	3
3	4
\.


--
-- Data for Name: warehouse; Type: TABLE DATA; Schema: coffee_shop_schema; Owner: postgres
--

COPY coffee_shop_schema.warehouse (warehouse_id, address, status, employee_id) FROM stdin;
1	Lam Ha	In stock	1
2	Tan Ha	In stock	1
3	Dan Phuong	In stock	1
4	Me Linh	In stock	1
\.


--
-- Name: bill_bill_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.bill_bill_id_seq', 5, true);


--
-- Name: customer_customer_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.customer_customer_id_seq', 4, true);


--
-- Name: employee_employee_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.employee_employee_id_seq', 5, true);


--
-- Name: main_log_log_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.main_log_log_id_seq', 21, true);


--
-- Name: orders_oder_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.orders_oder_id_seq', 4, true);


--
-- Name: product_product_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.product_product_id_seq', 6, true);


--
-- Name: secret_data_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.secret_data_id_seq', 2, true);


--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.supplier_supplier_id_seq', 3, true);


--
-- Name: warehouse_warehouse_id_seq; Type: SEQUENCE SET; Schema: coffee_shop_schema; Owner: postgres
--

SELECT pg_catalog.setval('coffee_shop_schema.warehouse_warehouse_id_seq', 4, true);


--
-- Name: bill bill_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.bill
    ADD CONSTRAINT bill_pkey PRIMARY KEY (bill_id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);


--
-- Name: main_log main_log_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.main_log
    ADD CONSTRAINT main_log_pkey PRIMARY KEY (log_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (product_id);


--
-- Name: secret_data secret_data_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.secret_data
    ADD CONSTRAINT secret_data_pkey PRIMARY KEY (id);


--
-- Name: supplier supplier_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (supplier_id);


--
-- Name: warehouse warehouse_pkey; Type: CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.warehouse
    ADD CONSTRAINT warehouse_pkey PRIMARY KEY (warehouse_id);


--
-- Name: idx_bill_order_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_bill_order_id ON coffee_shop_schema.bill USING btree (order_id);


--
-- Name: idx_customer_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_customer_id ON coffee_shop_schema.customer USING btree (customer_id);


--
-- Name: idx_imployee_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_imployee_id ON coffee_shop_schema.employee USING btree (employee_id);


--
-- Name: idx_order_customer_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_order_customer_id ON coffee_shop_schema.orders USING btree (customer_id);


--
-- Name: idx_order_employee_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_order_employee_id ON coffee_shop_schema.orders USING btree (employee_id);


--
-- Name: idx_order_product_order_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_order_product_order_id ON coffee_shop_schema.order_product USING btree (order_id);


--
-- Name: idx_order_product_product_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_order_product_product_id ON coffee_shop_schema.order_product USING btree (product_id);


--
-- Name: idx_product_warehouse_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_product_warehouse_id ON coffee_shop_schema.product USING btree (warehouse_id);


--
-- Name: idx_spplier_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_spplier_id ON coffee_shop_schema.supplier USING btree (supplier_id);


--
-- Name: idx_supplier_product_product_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_supplier_product_product_id ON coffee_shop_schema.supplier_product USING btree (product_id);


--
-- Name: idx_supplier_product_supplier_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_supplier_product_supplier_id ON coffee_shop_schema.supplier_product USING btree (supplier_id);


--
-- Name: idx_warehouse_employee_id; Type: INDEX; Schema: coffee_shop_schema; Owner: postgres
--

CREATE INDEX idx_warehouse_employee_id ON coffee_shop_schema.warehouse USING btree (employee_id);


--
-- Name: product bill_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER bill_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product customer_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER customer_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product employee_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER employee_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product order_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER order_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product product_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER product_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product supplier_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER supplier_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: product warehouse_logging; Type: TRIGGER; Schema: coffee_shop_schema; Owner: postgres
--

CREATE TRIGGER warehouse_logging AFTER INSERT OR DELETE OR UPDATE ON coffee_shop_schema.product FOR EACH ROW EXECUTE FUNCTION coffee_shop_schema.logging();


--
-- Name: bill bill_order_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.bill
    ADD CONSTRAINT bill_order_id_fkey FOREIGN KEY (order_id) REFERENCES coffee_shop_schema.orders(order_id);


--
-- Name: bill bill_order_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.bill
    ADD CONSTRAINT bill_order_id_fkey1 FOREIGN KEY (order_id) REFERENCES coffee_shop_schema.orders(order_id);


--
-- Name: order_product order_product_order_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.order_product
    ADD CONSTRAINT order_product_order_id_fkey FOREIGN KEY (order_id) REFERENCES coffee_shop_schema.orders(order_id);


--
-- Name: order_product order_product_order_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.order_product
    ADD CONSTRAINT order_product_order_id_fkey1 FOREIGN KEY (order_id) REFERENCES coffee_shop_schema.orders(order_id);


--
-- Name: order_product order_product_product_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.order_product
    ADD CONSTRAINT order_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES coffee_shop_schema.product(product_id);


--
-- Name: order_product order_product_product_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.order_product
    ADD CONSTRAINT order_product_product_id_fkey1 FOREIGN KEY (product_id) REFERENCES coffee_shop_schema.product(product_id);


--
-- Name: orders orders_customer_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES coffee_shop_schema.customer(customer_id);


--
-- Name: orders orders_customer_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders
    ADD CONSTRAINT orders_customer_id_fkey1 FOREIGN KEY (customer_id) REFERENCES coffee_shop_schema.customer(customer_id);


--
-- Name: orders orders_employee_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders
    ADD CONSTRAINT orders_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES coffee_shop_schema.employee(employee_id);


--
-- Name: orders orders_employee_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.orders
    ADD CONSTRAINT orders_employee_id_fkey1 FOREIGN KEY (employee_id) REFERENCES coffee_shop_schema.employee(employee_id);


--
-- Name: product product_warehouse_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.product
    ADD CONSTRAINT product_warehouse_id_fkey FOREIGN KEY (warehouse_id) REFERENCES coffee_shop_schema.warehouse(warehouse_id);


--
-- Name: supplier_product supplier_product_product_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier_product
    ADD CONSTRAINT supplier_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES coffee_shop_schema.product(product_id);


--
-- Name: supplier_product supplier_product_product_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier_product
    ADD CONSTRAINT supplier_product_product_id_fkey1 FOREIGN KEY (product_id) REFERENCES coffee_shop_schema.product(product_id);


--
-- Name: supplier_product supplier_product_supplier_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier_product
    ADD CONSTRAINT supplier_product_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES coffee_shop_schema.supplier(supplier_id);


--
-- Name: supplier_product supplier_product_supplier_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.supplier_product
    ADD CONSTRAINT supplier_product_supplier_id_fkey1 FOREIGN KEY (supplier_id) REFERENCES coffee_shop_schema.supplier(supplier_id);


--
-- Name: warehouse warehouse_employee_id_fkey; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.warehouse
    ADD CONSTRAINT warehouse_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES coffee_shop_schema.employee(employee_id);


--
-- Name: warehouse warehouse_employee_id_fkey1; Type: FK CONSTRAINT; Schema: coffee_shop_schema; Owner: postgres
--

ALTER TABLE ONLY coffee_shop_schema.warehouse
    ADD CONSTRAINT warehouse_employee_id_fkey1 FOREIGN KEY (employee_id) REFERENCES coffee_shop_schema.employee(employee_id);


--
-- Name: SCHEMA coffee_shop_schema; Type: ACL; Schema: -; Owner: postgres
--

GRANT USAGE ON SCHEMA coffee_shop_schema TO sales_role;
GRANT USAGE ON SCHEMA coffee_shop_schema TO warehouse_role;


--
-- Name: TABLE customer; Type: ACL; Schema: coffee_shop_schema; Owner: postgres
--

GRANT SELECT ON TABLE coffee_shop_schema.customer TO sales_role;


--
-- Name: TABLE orders; Type: ACL; Schema: coffee_shop_schema; Owner: postgres
--

GRANT SELECT ON TABLE coffee_shop_schema.orders TO sales_role;


--
-- Name: TABLE product; Type: ACL; Schema: coffee_shop_schema; Owner: postgres
--

GRANT SELECT,INSERT,UPDATE ON TABLE coffee_shop_schema.product TO warehouse_role;


--
-- Name: TABLE warehouse; Type: ACL; Schema: coffee_shop_schema; Owner: postgres
--

GRANT SELECT,INSERT ON TABLE coffee_shop_schema.warehouse TO warehouse_role;


--
-- PostgreSQL database dump complete
--

