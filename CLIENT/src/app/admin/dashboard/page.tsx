"use client"; // Ensure this is a client component

import Dashboard from "@/components/dashboard/dashboard";
import { Suspense, useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { Button } from "@/components/ui/button";

function Page() {
  const [search, setSearch] = useState("");

  return (
    <div className="p-6 space-y-4">
      {/* Search Bar for Quick Access */}
      <Input
        placeholder="Search dashboard..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full md:w-1/3 border rounded-lg p-2"
      />

      {/* Dashboard with Suspense (Ensure it's a client component) */}
      <Suspense fallback={<Skeleton className="h-96 w-full" />}>
        <Dashboard searchQuery={search} />
      </Suspense>

      {/* Quick Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardContent className="p-4">
            <h3 className="text-xl font-bold">Users</h3>
            <p className="text-lg text-gray-600">1,245 Active</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <h3 className="text-xl font-bold">Sales</h3>
            <p className="text-lg text-gray-600">$23,500</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <h3 className="text-xl font-bold">Tickets</h3>
            <p className="text-lg text-gray-600">78 Pending</p>
          </CardContent>
        </Card>
      </div>

      {/* Refresh Button */}
      <Button onClick={() => window.location.reload()} className="mt-4">
        Refresh
      </Button>
    </div>
  );
}

export default Page;

