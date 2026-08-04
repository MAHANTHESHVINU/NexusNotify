import { useState } from "react";

import Header from "../components/Header";
import MetricCard from "../components/MetricCard";
import NotificationTable from "../components/NotificationTable";
import DecisionPanel from "../components/DecisionPanel";
import AnalyticsCharts from "../components/AnalyticsCharts";

import { useMetrics } from "../hooks/useMetrics";
import { usePredictions } from "../hooks/usePrediction";

import type { Prediction } from "../types/prediction";

export default function Dashboard() {

    // Metrics
    const {
        metrics,
        loading,
    } = useMetrics();

    // Predictions
    const {
        predictions,
        loading: predictionLoading,
    } = usePredictions();

    // Selected notification
    const [selectedPrediction, setSelectedPrediction] =
        useState<Prediction | null>(null);

    // Search
    const [search, setSearch] = useState("");

    // Filter notifications
    const filteredPredictions = predictions.filter((prediction) => {

        const query = search.toLowerCase();

        return (
            prediction.message_id.toLowerCase().includes(query) ||
            prediction.action.toLowerCase().includes(query) ||
            prediction.message_type.toLowerCase().includes(query) ||
            prediction.reason.toLowerCase().includes(query)
        );

    });

    return (
        <div
            style={{
                padding: "30px",
                background: "#f3f4f6",
                minHeight: "100vh",
            }}
        >
            <Header />

            {/* KPI Cards */}

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    flexWrap: "wrap",
                    marginBottom: "25px",
                }}
            >
                <MetricCard
                    title="Accuracy"
                    value={
                        loading
                            ? "Loading..."
                            : metrics
                                ? `${(metrics.accuracy * 100).toFixed(2)}%`
                                : "N/A"
                    }
                />

                <MetricCard
                    title="Precision"
                    value={
                        loading
                            ? "Loading..."
                            : metrics
                                ? `${(metrics.precision * 100).toFixed(2)}%`
                                : "N/A"
                    }
                />

                <MetricCard
                    title="Recall"
                    value={
                        loading
                            ? "Loading..."
                            : metrics
                                ? `${(metrics.recall * 100).toFixed(2)}%`
                                : "N/A"
                    }
                />

                <MetricCard
                    title="F1 Score"
                    value={
                        loading
                            ? "Loading..."
                            : metrics
                                ? `${(metrics.f1_score * 100).toFixed(2)}%`
                                : "N/A"
                    }
                />
            </div>

            {/* Search */}

            <div
                style={{
                    marginBottom: "25px",
                }}
            >
                <input
                    type="text"
                    placeholder="🔍 Search by Message ID, Action, Type or Reason..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "14px",
                        borderRadius: "10px",
                        border: "1px solid #d1d5db",
                        fontSize: "15px",
                        outline: "none",
                    }}
                />
            </div>

            {/* Main Grid */}

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "2fr 1fr",
                    gap: "20px",
                    alignItems: "start",
                }}
            >
                <NotificationTable
                    predictions={filteredPredictions}
                    loading={predictionLoading}
                    onSelect={setSelectedPrediction}
                />

                <DecisionPanel
                    prediction={selectedPrediction}
                />
            </div>

            {/* Charts */}

            <AnalyticsCharts
                predictions={filteredPredictions}
            />
        </div>
    );
}