import dagster as dg

from dagster_duckdb import DuckDBResource

@dg.asset(
    deps=["customers", "orders", "payments"],
)
def orders_aggregation(duckdb: DuckDBResource):
    table_name = "orders_aggregation"

    with duckdb.get_connection() as conn:
        conn.execute(
            f"""
            create or replace table {table_name} as (
                select
                    c.id as customer_id,
                    c.first_name,
                    c.last_name,
                    count(distinct o.id) as total_orders,
                    count(distinct p.id) as total_payments,
                    coalesce(sum(p.amount), 0) as total_amount_spent
                from customers c
                left join orders o
                    on c.id = o.user_id
                left join payments p
                    on o.id = p.order_id
                group by 1, 2, 3
            );
            """
        )
