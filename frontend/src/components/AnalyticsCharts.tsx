import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
    CartesianGrid,
    XAxis,
    YAxis,
} from "recharts";

import type { Prediction } from "../types/prediction";

type Props = {
    predictions: Prediction[];
};

const COLORS = [
    "#3b82f6",
    "#22c55e",
    "#ef4444",
    "#f59e0b",
    "#8b5cf6",
];

export default function AnalyticsCharts({
    predictions,
}: Props) {

    const typeCounts = predictions.reduce((acc, prediction) => {

        acc[prediction.message_type] =
            (acc[prediction.message_type] || 0) + 1;

        return acc;

    }, {} as Record<string, number>);

    const pieData = Object.entries(typeCounts).map(
        ([name, value]) => ({
            name,
            value,
        })
    );

    const confidenceData = predictions.map((prediction) => ({
        id: prediction.message_id,
        confidence: Number(
            (prediction.confidence * 100).toFixed(1)
        ),
    }));

    return (
        <div
            style={{
                display: "grid",
                gridTemplateColumns: "1fr 1fr",
                gap: "20px",
                marginTop: "30px",
            }}
        >
            <div
                style={{
                    background: "white",
                    padding: "20px",
                    borderRadius: "12px",
                }}
            >
                <h3>Notification Types</h3>

                <ResponsiveContainer
                    width="100%"
                    height={300}
                >
                    <PieChart>
                        <Pie
                            data={pieData}
                            dataKey="value"
                            nameKey="name"
                            outerRadius={100}
                            label
                        >
                            {pieData.map((_, index) => (
                                <Cell
                                    key={index}
                                    fill={
                                        COLORS[
                                            index % COLORS.length
                                        ]
                                    }
                                />
                            ))}
                        </Pie>

                        <Tooltip />
                    </PieChart>
                </ResponsiveContainer>
            </div>

            <div
                style={{
                    background: "white",
                    padding: "20px",
                    borderRadius: "12px",
                }}
            >
                <h3>Confidence Scores</h3>

                <ResponsiveContainer
                    width="100%"
                    height={300}
                >
                    <BarChart
                        data={confidenceData}
                    >
                        <CartesianGrid strokeDasharray="3 3" />

                        <XAxis dataKey="id" hide />

                        <YAxis />

                        <Tooltip />

                        <Bar
                            dataKey="confidence"
                            fill="#3b82f6"
                        />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}