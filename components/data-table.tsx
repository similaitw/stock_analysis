type DataTableProps = {
  title: string;
  rows: Array<Record<string, unknown>>;
  emptyMessage: string;
};

function renderValue(value: unknown) {
  if (value === null || value === undefined || value === "") {
    return "-";
  }
  if (Array.isArray(value)) {
    return value.join(", ");
  }
  if (typeof value === "object") {
    return JSON.stringify(value);
  }
  return String(value);
}

export function DataTable({ title, rows, emptyMessage }: DataTableProps) {
  const columns = rows.length > 0 ? Object.keys(rows[0]) : [];

  return (
    <section className="panel">
      <div className="panel-header">
        <h2>{title}</h2>
        <span>{rows.length} 筆</span>
      </div>
      {rows.length === 0 ? (
        <p className="empty-state">{emptyMessage}</p>
      ) : (
        <div className="table-shell">
          <table>
            <thead>
              <tr>
                {columns.map((column) => (
                  <th key={column}>{column}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, rowIndex) => (
                <tr key={`${title}-${rowIndex}`}>
                  {columns.map((column) => (
                    <td key={`${title}-${rowIndex}-${column}`}>{renderValue(row[column])}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
