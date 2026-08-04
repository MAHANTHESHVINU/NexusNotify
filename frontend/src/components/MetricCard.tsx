type Props = {
    title: string;
    value: string;
};

export default function MetricCard({
    title,
    value,
}: Props) {

    return (
        <div
            style={{
                flex: 1,
                minWidth: "180px",
                background: "white",
                padding: "20px",
                borderRadius: "12px",
                boxShadow: "0 4px 10px rgba(0,0,0,.08)",
            }}
        >
            <p
                style={{
                    color: "#6b7280",
                    marginBottom: "10px",
                }}
            >
                {title}
            </p>

            <h2
                style={{
                    margin: 0,
                    color: "#2563eb",
                }}
            >
                {value}
            </h2>
        </div>
    );
}