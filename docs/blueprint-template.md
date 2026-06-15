# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [MEMBERS]:
  - Member 1: Nguyễn Đăng Khương | Role: Full Stack Observability (Logging, Tracing, SLOs, Alerts, Dashboard)

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 10
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: [Chèn link ảnh chụp màn hình file logs.jsonl hiển thị correlation_id tại đây]
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: [Chèn link ảnh chụp màn hình file logs.jsonl hiển thị [REDACTED_...] tại đây]
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: [Chèn link ảnh chụp màn hình giao diện Langfuse tại đây]
- [TRACE_WATERFALL_EXPLANATION]: RAG span chiếm thời gian đáng kể (latency) trong tổng thời gian xử lý yêu cầu, chứng tỏ phần lớn thời gian chờ là do việc truy vấn cơ sở dữ liệu vector hoặc tài liệu nội bộ.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: [Chèn link ảnh chụp giao diện Dashboard (Grafana/Datadog) của bạn tại đây]
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 818ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.02 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: [Chèn link ảnh chụp giao diện thiết lập Alert tại đây]
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#L4-L14

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Hệ thống bắt đầu kích hoạt cảnh báo P2 "high_latency_p95". Các câu lệnh truy vấn có thời gian phản hồi (latency) vọt lên rất cao, vượt qua ngưỡng 5000ms.
- [ROOT_CAUSE_PROVED_BY]: Xác minh qua Tracing (span của hàm `retrieve` trong RAG) và qua Log (có thời gian phản hồi tăng đột biến). Khẳng định thêm do biến trạng thái incident `rag_slow` đang ở mức True.
- [FIX_ACTION]: Vô hiệu hóa sự cố bằng lệnh API `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Thêm logic Timeout (ví dụ 3 giây) khi gọi hệ thống RAG và fallback (trả về kết quả default hoặc cache) thay vì để request bị treo quá lâu.

---

## 5. Individual Contributions & Evidence

### Nguyễn Đăng Khương
- [TASKS_COMPLETED]: Hoàn thành toàn bộ các hạng mục: cài đặt Correlation ID, bổ sung PII scrubber, liên kết context logs, tạo alerts, xử lý incident và viết báo cáo.
- [EVIDENCE_LINK]: (Chèn link commit/PR của bạn)

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
